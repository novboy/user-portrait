# -*- coding: utf-8 -*-
import time
import threading

from pybloom import BloomFilter

from app.database import Mysql, MongoDB

from app.basicinfo_crawler import BasicinfoCrawler
from app.tweets_crawler import TweetsCrawler
from app.relation_crawler import RelationCrawler

from UserProfile import UserProfileFromDicPart

LOCK = threading.Lock()

basicinfo_crawler = BasicinfoCrawler()
tweets_crawler = TweetsCrawler()
relation_crawler = RelationCrawler()

'''
全局变量
'''
USER_LIST = []
USER_LIST_TEMP = []
BLOOM_FILTER = BloomFilter(capacity = 2500000, error_rate = 0.001)

def extension_thread():
	i = 0

	while i < 2000000:
		user_id = USER_LIST_TEMP.pop(0)
		cursor = -1

		while cursor != 0:
			users_info = relation_crawler.get_friendids_paged_sleep(user_id = user_id, cursor = cursor)
			cursor = users_info[0]
			friend_list = users_info[2]
			
			for u in friend_list:
				u = str(u)
				
				if u not in BLOOM_FILTER:
					USER_LIST_TEMP.append(u)
					BLOOM_FILTER .add(u)

					i += 1

					if LOCK.acquire():
						USER_LIST.append(u)
						LOCK.release()


def portrayal_thread():
	db = MongoDB().connect()
	collect = db['user_portrayal']

	while len(USER_LIST) != 0:
		if LOCK.acquire():
			user_id = USER_LIST.pop(0)
			LOCK.release()

		user = get_user_info(user_id)

		if user == False:
			continue

		res = UserProfileFromDicPart(user)

		collect.insert_one(res)



def get_user_info(user_id):
	user = basicinfo_crawler.get_user(user_id = user_id)

	if not judge_available(user):
		return False

	tweets = tweets_crawler.get_user_all_timeline_temp(user_id = user_id)

	user = {
		'_id': user.id,
		'screen_name': user.screen_name,
		'name': user.name,
		'verified': user.verified,
		'friends_count': user.friends_count,
		'description': user.description,
		'crawler_date': time.strftime('%Y-%m-%d',time.localtime(time.time())),
		'followers_count': user.followers_count,
		'location': user.location,
		'statuses_count': user.statuses_count,
		'favourites_count': user.favourites_count,
		'lang': user.lang,
		'utc_offset': user.utc_offset,
		'protected': user.protected,
		'profile_background_color': user.profile_background_color,
		'default_profile_image': user.default_profile_image,
		'created_at': user.created_at,
		'profile_banner_url': user.profile_banner_url,
		'time_zone': user.time_zone,
		'profile_image_url': user.profile_image_url,
		'listed_count': user.listed_count,
		'tweets': tweets
	}

	return user

def judge_available(user):
	return user.lang == 'en' and user.statuses_count > 500 and user.protected == False and user.followers_count > 500


def main():
	db = MongoDB().connect()
	collect = db['typical']

	users = collect.find({}, {'_id': 1})

	for u in users:
		BLOOM_FILTER.add(str(u['_id']))
		USER_LIST_TEMP.append(str(u['_id']))

	collect = db['user_portrayal']
	users = collect.find({}, {'_id': 1})

	for u in users:
		BLOOM_FILTER.add(str(u['_id']))


	et = threading.Thread(target = extension_thread, args = ())
	et.start()

	time.sleep(1)

	i = 0
	thread_num = 3
	thread_pool = []
	
	while i < thread_num:
		it = threading.Thread(target = portrayal_thread, args = ())
		
		it.start()
		thread_pool.append(it)

		i += 1

	for thread in thread_pool:
		thread.join()

	et.join()


if __name__ == '__main__':
	main()
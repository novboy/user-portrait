from py2neo import Graph, Node, Relationship

from app.database import Neo4j, MongoDB

def create_relation():
	graph = Neo4j().connect()
	# mysql = Mysql().connect()
	mongo = MongoDB().connect()

	# graph = graph.delete_all()
	
	# tus = mongo['typical'].find({}, {'_id': 1})

	# for item in tus:
	# 	user = Node("Typical", user_id = item['_id'])
	# 	graph.create(user)

	tus = mongo['relation'].find({}, {'_id': 1})
	user_list = map(lambda item: item['_id'], tus)

	for user_id in user_list:
		friends = mongo['relation'].find_one({'_id': user_id})
		friends = set(friends['friends'])

		node1 = graph.find_one("Typical",
							   property_key = "user_id",
  							   property_value = user_id)

		for user_id1 in user_list:
			if user_id1 == user_id:
				continue

			if user_id1 in friends:
				node2 = graph.find_one("Typical",
							   		   property_key = "user_id",
  							   		   property_value = user_id1)

				following = Relationship(node1, 'following', node2)
				
				graph.create(following)


def update_attr():
	graph = Neo4j().connect()
	mongo = MongoDB().connect()

	tus = mongo['typical'].find({}, {'name': 1, 'category': 1, 'followers_count': 1, 'location': 1,
		'utc_offset': 1, 'statuses_count': 1, 'description': 1, 'friends_count': 1, 'psy': 1, 'verified': 1,
		'psy_tweets_starttime': 1, 'lang': 1, 'favourites_count': 1, 'screen_name': 1, 'influence_score': 1, 
		'created_at': 1, 'time_zone': 1, 'protected': 1, 'rank_influ': 1, 'activity': 1})

	for item in tus:
		node = graph.find_one("Typical",
							  property_key = "user_id",
  							  property_value = item['_id'])
		node['name'] = item['name']
		node['category'] = item['category']
		node['followers_count'] = item['followers_count']
		node['location'] = item['location']
		node['utc_offset'] = item['utc_offset']
		node['statuses_count'] = item['statuses_count']
		node['description'] = item['description']
		node['friends_count'] = item['friends_count']
		node['psy'] = item['psy']
		node['verified'] = item['verified']
		node['psy_tweets_starttime'] = item['psy_tweets_starttime']
		node['lang'] = item['lang']
		node['favourites_count'] = item['favourites_count']
		node['screen_name'] = item['screen_name']
		node['influence_score'] = item['influence_score']
		node['created_at'] = item['created_at']
		node['time_zone'] = item['time_zone']
		node['protected'] = item['protected']
		node['rank_influ'] = item['rank_influ']
		node['activity'] = item['activity']

		graph.push(node)


if __name__ == '__main__':
	# create_relation()
	update_attr()
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

# reqparse ->  Flask-RESTful's request parsing interface,It's designed to provide simple and uniform access to any variable on the flask.


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('title', required=True, dest='something')


videos = {
    'video1': {
        'title': 'Batman v Superman scene'
    },
    'video2': {
        'title': 'Superman and Alfred Meeting'
    }
}

class Video(Resource):
    
    def get(self, video_id):
        if video_id == "all":
            return videos   # shows both the keys and values assigned in the video dict
        
        if video_id not in videos:
            abort(404, message=f'Video {video_id} not found')
        return videos[video_id]
    
    
    def put(self, video_id):
        args = parser.parse_args()
        new_video = {'title': args['title']}

        videos[video_id] = new_video
        return {video_id: videos[video_id]}, 201


    def delete(self, video_id):
        if video_id not in videos:
            abort(404, message=f"Video {video_id} not found")
        del videos[video_id]
        return "", 204
    
class VideoSchedule(Resource):
    def get(self):
        return videos
    
    def post(self):
        args = parser.args()
        new_video = {'title': args['title']}
        video_id = max(int(v.lstrip('video')) for v in videos.keys()) + 1   # taking all the individual video id's and stripping away the video to end up with a number that gets converted into an integer and list of all and get a maximum from that list
        
        # lstrip() returns a copy of the string in which all chars have been stripped from the beginning of the string (default whitespace characters).
        videos[video_id] = f'video {video_id}'
        videos[video_id] = new_video
        return videos['video_id'], 201
    
    
api.add_resource(Video, '/videos/<video_id>')
api.add_resource(VideoSchedule, '/videos')


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
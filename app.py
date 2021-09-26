from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


videos = {
    'video1': {
        'title': 'Batman v Superman scene'
    },
    'video2': {
        'title': 'Superman and Alfred Meeting'
    }
}

class VideoScheduler(Resource):
    
    def get(self, video_id):
        if video_id == "all":
            return videos   # shows both the keys and values assigned in the video dict
        return videos[video_id]
    
    
api.add_resource(VideoScheduler, '/videos/<video_id>')

if __name__ == "__main__":
    app.run(debug=True)
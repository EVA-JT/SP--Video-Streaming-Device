user_data = {}

quality_list = ["low", "medium", "high"]

genres_list = ["action", "comedy", "romance"]
categories_list = ["movies", "shows"]

rating_list = {
    0:"All ages",
    10:"10+",
    12:"12",
    14:"14",
    16:"16",
    18:"18+"
}

movie_catalog = {
    "action movie 1": {
        "category": "movie",
        "genre": "action",
        "description": "sample sample",
        "year": "1990",
        "rating": 10,
        "reviews": {
            "Gabriel":{"score":10, "review":"Awesome."},
            "sample2":{"score":8, "review":""}
        }
    },
    "action movie 2": {
        "category": "movie",
        "genre": "action",
        "description": "sample sample",
        "year": "2001",
        "rating": 18,
        "reviews": {
            "joca":{"score":1, "review":"trash"},
            "sample2":{"score":3, "review":""}
        }
    },
    "action movie 3": {
        "category": "movie",
        "genre": "action",
        "description": "sample sample",
        "year": "2005",
        "rating": 0, 
        "reviews": {
            "zeca":{"score":7, "review":"It's okay."},
            "sample2":{"score":10, "review":""}
        }
    },
    "comedy movie 1":{
        "category": "movie",
        "genre": "comedy",
        "description": "sample sample",
        "year": "1990",
        "rating": 10,
        "reviews": {
            "Teteu":{"score":10, "review":"Cinema"},
            "sample2":{"score":8, "review":""}
        }
    },
    "comedy movie 2":{
        "category": "movie",
        "genre": "comedy",
        "description": "sample sample",
        "year": "2001",
        "rating": 18,
        "reviews": {
            "Bainao":{"score":5, "review":"Great for background noise"},
            "sample2":{"score":4, "review":""}
        }
    },
    "comedy movie 3":{
        "category": "movie",
        "genre": "comedy",
        "description": "sample sample",
        "year": "2005",
        "rating": 0,
        "reviews": {
            "Fox":{"score":8, "review":"An odyssey of humour."},
            "sample2":{"score":8, "review":""}
        }
    },
    "romance movie 1":{
        "category": "movie",
        "genre": "romance",
        "description": "sample sample",
        "year": "1990",
        "rating": 10,
        "reviews": {
            "Fry":{"score":7, "review":""},
            "sample2":{"score":9, "review":""}
        }
    },
    "romance movie 2":{
        "category": "movie",
        "genre": "romance",
        "description": "sample sample",
        "year": "2001",
        "rating": 18,
        "reviews": {
            "Pou":{"score":10, "review": "Got me in tears."},
            "sample2":{"score":8, "review":""}
        }
    },
    "romance movie 3":{
        "category": "movie",
        "genre": "romance",
        "description": "sample sample",
        "year": "2005",
        "rating": 0,
        "reviews": {
            "wol":{"score:":0, "review":"Are you kidding me?"},
            "sample2":{"score":1, "review":""}
        }
    }
}

show_catalog = {
    "action show 1": {
        "category": "show",
        "genre": "action",
        "description": "sample sample",
        "year": "1990",
        "rating": 10,
        "reviews": {
            "Sample":{"score":7, "review":"sample"},
            "sample2":{"score":8, "review":""}
        }
    },
    "action show 2": {
        "category": "show",
        "genre": "action",
        "description": "sample sample",
        "year": "2001",
        "rating": 18,
        "reviews": {
            "sample":{"score":10, "review":"sample"},
            "sample2":{"score":5, "review":""}
        }
    },
    "action show 3": {
        "category": "show",
        "genre": "action",
        "description": "sample sample",
        "year": "2005",
        "rating": 0,
        "reviews": {
            "sample":{"score":3, "review":"sample"},
            "sample2":{"score":5, "review":""}
        }
    },
    "comedy show 1":{
        "category": "show",
        "genre": "comedy",
        "description": "sample sample",
        "year": "1990",
        "rating": 10,
        "reviews": {
            "sample":{"score":6, "review":"sample"},
            "sample2":{"score":8, "review":""}
        }
    },
    "comedy show 2":{
        "category": "show",
        "genre": "comedy",
        "description": "sample sample",
        "year": "2001",
        "rating": 18,
        "reviews": {
            "sample":{"score":10, "review":"sample"},
            "sample2":{"score":10, "review":""}
        }
    },
    "comedy show 3":{
        "category": "show",
        "genre": "comedy",
        "description": "sample sample",
        "year": "2005",
        "rating": 0,
        "reviews": {
            "sample":{"score":4, "review":"sample"},
            "sample2":{"score":6, "review":""}
        }
    },
    "romance show 1":{
        "category": "show",
        "genre": "romance",
        "description": "sample sample",
        "year": "1990",
        "rating": 10,
        "reviews": {
            "sample":{"score":8, "review":"sample"},
            "sample2":{"score":8, "review":""}
        }
    },
     "romance show 2":{
        "category": "show",
        "genre": "romance",
        "description": "sample sample",
        "year": "2001",
        "rating": 18,
        "reviews": {
            "sample":{"score":0, "review":"sample"},
            "sample2":{"score":8, "review":""}
        }
    },
    "romance show 3":{
        "category": "show",
        "genre": "romance",
        "description": "sample sample",
        "year": "2005",
        "rating": 0,
        "reviews": {
            "sample":{"score":8, "review":"sample"},
            "sample2":{"score":5, "review":""}
        }
    }
}

ad = {
    "banner":{
        "ad_placement1":"sample",
        "ad_placement2":"sample",
        "ad_placement3":"sample"
    },
    "placement":{
        "movie":{

        },
        "show":{

        }
    }
}

all_catalog = {
    "movie": movie_catalog,
    "show": show_catalog
}

var mongo = require('mongodb');

var ConnMongoDB = function(){
    var db = new mongo.Db(
        'dateWeb',
        new mongo.Server(
            'localhost',
            27017,
            {}
        ),
        {}
    );
    return db;
}


module.exports = function(){
    return ConnMongoDB
}
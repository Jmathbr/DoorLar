var express = require('express'),
    bodyParser = require('body-parser'),
    mongodb = require('mongodb');
    objectId = require('mongodb').ObjectId;

var app = express();

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

var port = 3000;

app.listen(port);

console.log("Servidor executando: "+port);

var db = new mongodb.Db(
    'DoorLar',
    new mongodb.Server('localhost',27017,{}),
    {}
);

app.get('/', function(req, res){
    res.send({msg:'Olá'});
});

// Method POST(create)
app.post('/api', function(req, res){
    var dados = req.body;
    db.open(function(err, mongoclient){
        mongoclient.collection('user', function(err, collection){
            collection.insert(dados, function(err, records){
                if(err){
                    res.json({'status': 'erro'});
                }else{
                    res.json({'status': 'inclusao realizada com sucesso'});
                }
                mongoclient.close();
            });
        });
    });
});

// Method GET(ready)
app.get('/api', function(req, res){
    db.open(function(err, mongoclient){
        mongoclient.collection('user', function(err, collection){
            collection.find().toArray(function(err, results){
                if(err){
                    res.json(err);
                }else{
                    res.json(results);
                }
                mongoclient.close();
            });
        });
    });
});
// Method GET (ready Id)
app.get('/api/:id', function(req, res){
    db.open(function(err, mongoclient){
        mongoclient.collection('user', function(err, collection){
            collection.find(objectId(req.params.id)).toArray(function(err, results){
                if(err){
                    res.json(err);
                }else{
                    res.status(200).json(results);
                }
                mongoclient.close();
            });
        });
    });
});

// Method Put (update)
app.put('/api/:id', function(req, res){
    db.open(function(err, mongoclient){
        mongoclient.collection('user', function(err, collection){
            collection.update(
                {_id: objectId(req.params.id)},
                { $set: {nome : req.body.nome}},
                {},
                function(err,records){
                    if(err){
                        res.json(err);
                    }else{
                        res.json(records);
                    }
                mongoclient.close();
                }
                
            );
        });
    });
});
// Method Delete json
app.delete('/api/:id', function(req, res){
    db.open(function(err, mongoclient){
        mongoclient.collection('user', function(err, collection){
            collection.remove({_id: objectId(req.params.id)},function(err,records){
                if(err){
                    res.json(res);
                }else{
                    res.json(records)
                }
                mongoclient.close();
            });
        });
    });
});
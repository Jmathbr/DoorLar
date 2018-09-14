function UsuariosDAO(connection){
    this._connection = connection();
}

UsuariosDAO.prototype.inserirUsuario = function(usuario){
    this._connection.open(function(err,mongoclient){
        mongoclient.collection("usuarios", function(err,collection){
            collection.insert(usuario);
            mongoclient.close();
        })
    });
}
//pesquisando por id e inserindo a tag
UsuariosDAO.prototype.UpdateTag = function(Matricula,tag, req, res){
    this._connection.open(function(err,mongoclient){
        if (err) throw err;
        var myquery = {  matricula: Matricula  };
        var newvalues = { $set: { tag: "111111111111111" } };

        mongoclient.collection("usuarios", function(err,collection){

            collection.updateMany(myquery, newvalues, function(err, res) {
                if (err) throw err;
                console.log("TagCadastrada");
                mongoclient.close();
            })
        })
    });
}

UsuariosDAO.prototype.autenticar = function(usuario, req, res){
    this._connection.open(function(err,mongoclient){
        mongoclient.collection("usuarios", function(err,collection){
            collection.find(usuario).toArray(function(err,result){
                if(result[0] != undefined){
                    req.session.autorizado = true;
                    req.session.classe = result[0].classe; 
                    console.log(req.session._id = result[0]._id);
                }
                if(req.session.autorizado == true){
                    if(req.session.classe == 'SU'){
                        res.redirect('/admin')
                    }
                    else{
                        res.redirect('/user')
                    }
                }
                else{
                    res.render('home/index',{validacao:{}})
                }
            })

            mongoclient.close();
        })
    });
}

module.exports = function(){
    return UsuariosDAO;
}
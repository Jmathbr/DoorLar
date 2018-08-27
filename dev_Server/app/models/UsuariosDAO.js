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

UsuariosDAO.prototype.autenticar = function(usuario, req, res){
    this._connection.open(function(err,mongoclient){
        mongoclient.collection("usuarios", function(err,collection){
            collection.find(usuario).toArray(function(err,result){
                console.log(result.length)
                console.log(collection.find(usuario))
                if(result[0] != undefined){
                    req.session.autorizado = true;
                    req.session.classe = result[0].classe; 
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
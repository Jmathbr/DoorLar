function UsuariosDAO(connection){
    this._connection = connection();
}

UsuariosDAO.prototype.inserirUsuario = function(usuario){
    this._connection.open(function(err,mongoclient){
        mongoclient.collection("usuarios", function(err,collection){
            console.log("Usuario: ",usuario["nome"]," - Cadastrou")
            collection.insert(usuario);
            mongoclient.close();
        })
    });
}
//pesquisando por id e inserindo a tag
UsuariosDAO.prototype.UpdateTag = function(Matricula,tag, req, res){
    this._connection.open(function(err,mongoclient){
        if (err) throw err;
        var myquery = {  matricula: Matricula  };           //dado que eu quero procurar{endereço:dado}
        var newvalues = { $set: { tag: tag } };     // setando novos valores {endereço:dado}

        mongoclient.collection("usuarios", function(err,collection){

            collection.updateOne(myquery, newvalues, function(err, res) {
                if (err) throw err;
                console.log("Tag Cadastrada:",tag);
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
                    req.session.matricula = result[0].matricula;
                }
                console.log("Usuario: ",result[0].nome," - entrou")
                if(req.session.autorizado == true){
                    if(req.session.classe == 'SU'){
                        res.redirect('/admin')
                    }
                    else{
                        //console.log(req.body)         //Recupera os dados que foram fornecidos na pagina
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
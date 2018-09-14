module.exports.admin = function(app, req, res){
    if(req.session.autorizado == true){
        if(req.session.classe == 'SU'){
            res.render('admin')
        }
        else{
            res.render('user')
        }
    }
    else{
        res.render("home/index",{validacao:{}})
    }
}

module.exports.user = function(app, req, res){
    if((req.session.autorizado == true)&&(req.session.classe != 'SU')){
        res.render('user')
    }
    else{
        res.render("home/index",{validacao:{}})
    }
}

module.exports.sair = function(app, req, res){
    req.session.destroy(function(err){
        res.render('home/index',{validacao:{}})
    })
}

module.exports.abrir = function(app, req, res){
    if(req.session.autorizado == true){
        
        const axios = require('axios');
        username = '123';
        axios.get('http://10.6.4.110:8011/?Matricula=' + username)
        .then(function(response){
        console.log(response.data); // ex.: { user: 'Your User'}
        console.log(response.status);
        console.log('abrir1') // ex.: 200
        })
        
        if(req.session.classe == 'SU'){
            res.redirect('admin')
        }
        else{
            res.redirect('user')
        }
    }
    else{
        res.render("home/index",{validacao:{}})
    }
}

module.exports.tag = function(app, req, res){
    res.render('usrq/tag', {validacao: {},dadosForm: {}});
    console.log('renderizando tag')
}

module.exports.tagr = function(app, req, res){
    var dadosForm = req.body;
    req.assert('tag',' As senhas nao sao iguais').notEmpty();
    console.log("asdasdas");
    var connection = app.config.dbConnection;
    var UsuariosDAO = new app.app.models.UsuariosDAO(connection);

    UsuariosDAO.inserirUsuario(dadosForm)
    if(req.session.autorizado == true){
        if(req.session.classe == 'SU'){
            res.render('admin')
        }
        else{
            res.render('user')
        }
    }
}
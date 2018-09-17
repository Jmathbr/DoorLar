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
    //tem que dar um get com o axios no esp
    //solicitando o cadastro, por exemplo
    //metodo q, quando metodo 1 for passado por get,
    //o esp vai esperar a tag e logo em seguida dar um post na tag
    var matricula = req.session.matricula //tenho que conseguir pegar essa variavel na hora de logar

    var dadosForm = req.body;
    req.assert('tag',' As senhas nao sao iguais').notEmpty();
    
    var connection = app.config.dbConnection;
    var UsuariosDAO = new app.app.models.UsuariosDAO(connection);
    UsuariosDAO.UpdateTag(matricula,dadosForm)
    if(req.session.autorizado == true){
        if(req.session.classe == 'SU'){
            res.render('admin')
        }
        else{
            res.render('user')
        }
    }
}
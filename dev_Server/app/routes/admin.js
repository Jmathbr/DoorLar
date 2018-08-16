module.exports = function(app){
    app.get('/admin', function(req,res){
        app.app.controllers.admin.admin(app, req, res)
    })

    app.get('/user', function(req,res){
        app.app.controllers.admin.user(app, req, res)
    })
    
    app.get('/sair', function(req,res){
        app.app.controllers.admin.sair(app, req, res)
    })

    app.get('/abrir', function(req,res){
        const axios = require('axios');
        username = '123';
        axios.get('hhttp://10.6.4.110:8011/?Matricula=' + username)
        .then(function(response){
        console.log(response.data); // ex.: { user: 'Your User'}
        console.log(response.status); // ex.: 200
    })
    
  }); 
}
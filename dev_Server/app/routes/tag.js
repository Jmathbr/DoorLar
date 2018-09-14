module.exports = function(app){
    app.get('/tag', function(req,res){
        app.app.controllers.admin.tag(app, req, res)
    })
    app.post('/tagr', function(req,res){
        app.app.controllers.admin.tagr(app, req, res)
    })
    app.get('/sair', function(req,res){
        app.app.controllers.admin.tagr(app, req, res)
    })
}
module.exports.home = function(app, req, res){
    res.render('home/index',{validacao:{}});
}
module.exports.autenticar = function(app, req, res){

    var dadosForm = req.body;
    
    req.assert('email','Email nao pode ser vazio').isEmail();
    req.assert('senha','Senha nao pode ser vazio').notEmpty();
    
    var erros = req.validationErrors();
    
    if(erros){
        res.render('home/index',{validacao: erros, dadosForm: dadosForm})
        return;
    }
    console.log(dadosForm.email)
    var connection = app.config.dbConnection;
    var UsuariosDAO = new app.app.models.UsuariosDAO(connection);

    UsuariosDAO.autenticar(dadosForm, req, res);

}
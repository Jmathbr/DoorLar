module.exports.cadastro = function(app, req, res){
    res.render('usrq/cadastro', {validacao: {},dadosForm: {}});
}
module.exports.cadastrar = function(app, req, res){

    var dadosForm = req.body;

    req.assert('nome',' Nome nao pode ser vazio').notEmpty();
    req.assert('email',' Email nao pode ser vazio, ou formato de email nao aceito').isEmail();
    req.assert('matricula',' Matricula nao pode ser vazio').isNumeric();
    req.assert('senha',' Senha nao pode ser vazio').notEmpty();
    req.assert('senha',' As senhas nao sao iguais').equals(dadosForm.rsenha);

    var erros = req.validationErrors();
    dadosForm.classe = 'C';
    dadosForm.tag = '01010101';
    if(erros){
        res.render('usrq/cadastro',{validacao: erros, dadosForm: dadosForm})
        return;
    }
    else{
        res.render("home/index")
    }
    var connection = app.config.dbConnection;
    var UsuariosDAO = new app.app.models.UsuariosDAO(connection);

    UsuariosDAO.inserirUsuario(dadosForm)
    
    res.redirect("/")
}
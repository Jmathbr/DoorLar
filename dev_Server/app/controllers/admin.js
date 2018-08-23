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
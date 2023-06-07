create database bdescola; 
use bdescola;
create table aluno (
	codigo int primary key auto_increment,
    nome varchar(50),
    endereco varchar(50),
    telefone varchar(50)
    );
insert into aluno(nome,endereco,telefone) values ('João', 'Av.teste', '111111');
select * from aluno;    
update aluno set nome= "joãoTeste"
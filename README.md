# SEARCH ARTICLES

Scientific research is part of lives of reasearchers and academic specialists. 
This project aims to create a web platform that make life easier to researchers offering 
a quick and assertive search for scientific articles.

### Adding data
To populate database you must provide a json file per table inside `api/fixtures/` folder. The name
 of each file must be the name of the class that define the table. 

After that, use the `upload_data` custom command to upload. This command needs a `--model` option.
If model has f-keys use the option `--foreign-key` and if your json file has keys that is not in you
table structure use the `--not_use` option. 

Below there are some examples of use of this command.
```shell
./manage.py upload_data -m TblServidores -f CodCargo CodSiglaOrgaoIE -n NumSiape CodJornadaTrab CodOrgaoIEExerc DatIngressoOrgao AnoIngressoOrgao ValTempoServicoIE CodLattes FlagPesquisador
```

```shell
./manage.py upload_data -m TblArtigoPublicado -f CodSiglaAtuacaoProfissionalLattes CodIssn CodTitulosArtigos CodIdioma CodServidor -n CodLattes ID_ARTIGO CodDoi
```

```shell
./manage.py upload_data -m TblPalavraChaveArt
```

```shell

```

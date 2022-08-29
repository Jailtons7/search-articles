## Uploading data

Sice some tables could depend on keys in anothers (Foreign keys) this is the recommended order to upload data:
- TblOrgaoIeExerc
- TblCargos
- TblServidores
- TblIssn
- TblIdioma
- 
#### Uploading data TblCargos
```shell
python manage.py upload_data -m TblCargos
```

#### Uploading data TblOrgaoIeExerc
```shell
python manage.py upload_data -m TblOrgaoIeExerc
```

#### Uploading data TblServidores
```shell
python manage.py upload_data -m TblServidores -f CodCargo CodSiglaOrgaoIE -n NumSiape CodJornadaTrab CodOrgaoIEExerc DatIngressoOrgao AnoIngressoOrgao ValTempoServicoIE CodLattes FlagPesquisador
```

#### Uploading data TblIssn
```shell
python manage.py upload_data -m TblIssn
```

#### Uploading data TblIdioma
```shell
python manage.py upload_data -m TblIdioma
```

#### Uploading data TblArtigoPublicado
```shell
python manage.py upload_data -m TblArtigoPublicado -f CodSiglaAtuacaoProfissionalLattes CodIssn CodTitulosArtigos CodIdioma CodServidor -n CodLattes ID_ARTIGO CodDoi
```

#### Uploading data TblGrandeArea
```shell
python manage.py upload_data -m TblGrandeArea
```

#### Uploading data TblArea
```shell
python manage.py upload_data -m TblArea
```

#### Uploading data TblSubArea
```shell
python manage.py upload_data -m TblSubArea -f CodGrandeArea CodArea
```

#### Uploading data TblEspecialidade
```shell
python manage.py upload_data -m TblEspecialidade -f CodGrandeArea CodArea CodSubArea
```

#### Uploading data TblSituacao
```shell
python manage.py upload_data -m TblSituacao
```

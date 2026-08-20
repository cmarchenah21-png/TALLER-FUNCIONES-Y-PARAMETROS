def inicializar_db(host, puerto, db_name, usuario, password):
    print("Base de datos inicializada")


config = {
    "host": "cluster-db.internal",
    "puerto": 5432,
    "db_name": "production_v2",
    "usuario": "app_user",
    "password": "S3cur3P@ss!"
}

inicializar_db(**config)
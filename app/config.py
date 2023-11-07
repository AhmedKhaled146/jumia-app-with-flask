class Config:
    @staticmethod
    def init_app():
        pass





class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.sqlite'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost:5432/flasky_app'


project_config = {
     'dev': DevelopmentConfig,
     'prd': ProductionConfig,
}

"""Data models."""
# from infocodest import db
from app.extensions import db


class Metrica(db.Model):
    """Data model for user accounts."""

    __tablename__ = "metricas"

    id = db.Column(db.Integer, primary_key=True)
    repo = db.Column(db.String(64), unique=True, nullable=False)
    aplicacion = db.Column(db.String(64), unique=False, nullable=True)
    fecha = db.Column(db.String(64), unique=False, nullable=True)
    bugs = db.Column(db.Integer, index=True, unique=True, nullable=False)
    reliability_rating = db.Column(db.Integer, index=True, unique=True, nullable=False)
    reliability_label = db.Column(db.String(64), unique=False, nullable=True)
    vulnerabilities = db.Column(db.Integer, index=True, unique=True, nullable=False)
    security_rating = db.Column(db.Integer, index=True, unique=True, nullable=False)
    security_label = db.Column(db.String(64), unique=False, nullable=True)
    code_smells = db.Column(db.Integer, index=True, unique=True, nullable=False)
    sqale_rating = db.Column(db.Integer, index=True, unique=True, nullable=False)
    sqale_label = db.Column(db.String(64), unique=False, nullable=True)
    alert_status = db.Column(db.String(64), unique=False, nullable=True)
    project = db.Column(db.String(64), unique=False, nullable=True)
    complexity = db.Column(db.Integer, index=True, unique=True, nullable=False)
    coverage = db.Column(db.Integer, index=True, unique=True, nullable=False)
    unit_tests = db.Column(db.String(64), unique=False, nullable=True)
    ncloc = db.Column(db.Integer, index=True, unique=True, nullable=False)
    duplicated_line_density = db.Column(
        db.Integer, index=True, unique=True, nullable=False
    )
    sqale_index = db.Column(db.Integer, index=True, unique=True, nullable=False)
    sqale_debt_ratio = db.Column(db.Integer, index=True, unique=True, nullable=False)
    size = db.Column(db.String(64), unique=False, nullable=True)
    dloc_label = db.Column(db.String(64), unique=False, nullable=True)
    coverage_label = db.Column(db.String(64), unique=False, nullable=True)
    quality_gate = db.Column(db.String(64), unique=False, nullable=True)

    def __repr__(self):
        return "<Metrica {}>".format(self.aplicacion)

    def to_dict(self):
        return {
                c.name: str(getattr(self, c.name)) for c in self.__table__.columns
            }
        
class Proveedor(db.Model):
    """Data model for user accounts."""

    __tablename__ = "proveedor"

    id = db.Column(db.Integer, primary_key=True)
    aplicacion = db.Column(db.String(64), index=False, unique=True, nullable=False)
    proveedor = db.Column(db.Text, index=False, unique=False, nullable=True)
    tipo = db.Column(db.Text, index=False, unique=False, nullable=True)


    def __repr__(self):
        return "<Proveedor {}>".format(self.aplicacion)

    def to_dict(self):
        return {
                c.name: str(getattr(self, c.name)) for c in self.__table__.columns
            }

class Stat(db.Model):
    """Data model for user accounts."""

    __tablename__ = "stats"

    id = db.Column(db.Integer, primary_key=True)
    aplicacion = db.Column(db.String(64), index=False, unique=True, nullable=False)
    repos = db.Column(db.Integer, index=True, unique=True, nullable=False)
    reliability_label = db.Column(db.Text, index=False, unique=False, nullable=True)
    reliability_rating = db.Column(
        db.Integer, index=False, unique=False, nullable=False
    )
    sqale_label = db.Column(db.Text, index=False, unique=False, nullable=True)
    sqale_rating = db.Column(db.Integer, index=False, unique=False, nullable=False)
    security_label = db.Column(db.Text, index=False, unique=False, nullable=True)
    security_rating = db.Column(db.Integer, index=False, unique=False, nullable=False)
    alert_status_label = db.Column(db.Text, index=False, unique=False, nullable=True)
    alert_status_ok = db.Column(db.Integer, index=False, unique=False, nullable=False)
    dloc_label = db.Column(db.Text, index=False, unique=False, nullable=True)
    dloc_rating = db.Column(db.Integer, index=False, unique=False, nullable=False)
    coverage_label = db.Column(db.Text, index=False, unique=False, nullable=True)
    coverage_rating = db.Column(db.Integer, index=False, unique=False, nullable=False)

    def __repr__(self):
        return "<Stat {}>".format(self.aplicacion)

class Daily(db.Model):
    """Data model for user accounts."""

    __tablename__ = "daily"

    id = db.Column(db.Integer, primary_key=True)
    aplicacion = db.Column(db.String(64), index=False, unique=True, nullable=False)
    repo = db.Column(db.Integer, index=True, unique=True, nullable=False)
    proveedor = db.Column(db.Text, index=False, unique=False, nullable=True)
    created_on = db.Column(db.DateTime(), unique=False, nullable=True)
    num_bugs = db.Column(db.Integer, index=False, unique=False, nullable=False)
    num_vulnerabilities = db.Column(db.Integer, index=False, unique=False, nullable=False)
    num_code_smells = db.Column(db.Integer, index=False, unique=False, nullable=False)
    num_quality = db.Column(db.Integer, index=False, unique=False, nullable=False)
    num_analisis = db.Column(db.Integer, index=False, unique=False, nullable=False)

    def __repr__(self):
        return "<Daily {}>".format(self.aplicacion)
    
    def to_dict(self):
        return {
                c.name: str(getattr(self, c.name)) for c in self.__table__.columns
        }

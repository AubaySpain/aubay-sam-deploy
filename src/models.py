from pydantic import BaseModel


class CustomSettings(BaseModel):
    displayQR: bool = False


class ConfigLocale(BaseModel):
    default: dict[str, str | None] = {}


class Parameters(BaseModel):
    name: str = ''
    value: str = ''
    valueType: str = ''


class Templates(BaseModel):
    name: str = ''
    attachmentType: str = ''
    mediaType: str = ''
    originalFileName: str = ''
    description: str = ''


class ReportDefinition(BaseModel):
    reportType: str = ''
    filterName: str = ''
    formatType: str = ''
    name: str = ''
    cron: str = ''
    templateName: str = ''
    customSettings: dict[str, str] = {}


class AlarmsDefinition(BaseModel):
    alarmName: str = ''
    alarmSeverity: str = ''


class AssetLinks(BaseModel):
    configName: str = ''
    grantedFields: list[str] = []


class LinksDefinition(BaseModel):
    parentAssetLinks: list[AssetLinks] = []
    childAssetLinks: list[AssetLinks] = []


class YAMLModel(BaseModel):
    name: str = ''
    publishBlockchain: bool = False
    publishCertificates: bool = False
    publishPrivateCertificate: bool = False
    description: str = ''
    customSettings: CustomSettings = CustomSettings
    configLocale: ConfigLocale = ConfigLocale
    parameters: list[Parameters] = []
    templates: list[Templates] = []
    # configDefinition: list[ConfigDefinition] = []
    reportDefinition: list[ReportDefinition] = []
    alarmsDefinition: list[AlarmsDefinition] = []
    # rulesDefinition: list[RulesDefinition] = []
    linksDefinition: LinksDefinition = LinksDefinition

import dateutil.parser
import babel

def convertRowToObject( row):
    result = {}
    for column in row.__table__.columns:
      result[column.name] = getattr(row, column.name)
    
    return result

def convertTableToList( table):
    result = []
    for row in table:
        rowObj = convertRowToObject(row)
        result.append(rowObj)
    
    return result


def format_datetime(value, format='medium'):
  if isinstance(value, str):
    date = dateutil.parser.parse(value)
  else:
    date = value
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')
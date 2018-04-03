## Mini CMS

#### Dependencies
- Python 3.5+
- Virtualenv
- Django 2.0+
- Node 4.0+
- npm 3.0+

#### Setup Development
- Clone the repository
- create virtualenv
- Install packages.. `$ pip install -r requirements.txt`
- Create a database and copy `blackbox/config/db_config.py.txt` to `blackbox/config/db_config.py` and setup as django documentation and your desired db system
- Run `$ npm install`
- Run `$ npm run dev`

#### Production build
- Run `$ npm run build`
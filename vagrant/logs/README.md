# Logs Analysis Project
A simple program to extract information from a database that has more than 1.5M data stored.

## Objective
**It extract the followings:**
- The Top 3 most popluar Articles.
- Top Authors sorted by most viewed.
- Days of wich has more than 1% error requests.

## How to operate it?:

1. open your Terminal and navigate to the directory named `logs`.
2. boot up the virtual machine by running the command `vagrant up`.
3. then connect to it with `vagrant ssh`.
4. cd into the project with `cd /vagrant/logs`.
5. load the `news` table with `psql -d news -f newsdata.sql` and create the _views_ in the _Views details_ section below.
6. Run the project using `python report_generator.py`
	- the program should run and generate a report with the file name `report.txt`.
	_**note**: the file will be created if it's not available._


## Requirements
### views
These views are stored in the database and can be accessed through the VM by typing by these commands:
- `psql news`
- `\dv`

### Views details:
#### - error
To view **`error`** table type: `select * from error;`
```
CREATE view error as
select count(*) as errors, time::date as date
from log
where status like '%4%'
group by date;
```

#### - total
To view **`total`** table type: `select * from total;`
```
CREATE view total as
select count(*) as num, time::date as date
from log
group by date;
```
### Packages
To know more about the packages in this project type `pip list` while connected to the VM

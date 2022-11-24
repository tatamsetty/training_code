-- WWW.GITHUB.COM/TINITIATE

CREATE SCHEMA emp;
ALTER SCHEMA emp OWNER TO syntaxboard;

/*
Dept
DeptID(PK)  Dname string(100)   DirectorName   BuildingNumber  ContactNumber
1           Sales
2           Maktg
3           IT
4           Admin
*/

Create table dept (
    deptid  integer
   ,dname   varchar(100)
);
-- Add Primary Key 
alter table dept add constraint pk_dept PRIMARY key (deptid);

insert into dept values(1,'SALES');
insert into dept values(2,'MKTG');
insert into dept values(3,'IT');
insert into dept values(4,'Admin');

-- DSL
select * from dept;
select * from emp.dept;

/*                    
Emp
EmpID(PK)  Ename   Sal   decimal(7,2)    DeptID(FK)
1          A       1000.00                1
2          B       2000.00                2 
3          C       3000.00                3
4          D       1000.00                1
5          A       2000.00                3
6          F       1000.00                null
*/                    
Create table Emp (
    EmpID    integer
   ,Ename    varchar(100)
   ,sal      decimal(7,2)
   ,deptid   integer
);

-- Add Primary Key 
alter table Emp add constraint pk_Emp PRIMARY key (EmpID);
-- Add Foreign Key
ALTER TABLE Emp ADD CONSTRAINT FK_emp_deptid FOREIGN KEY (deptid) REFERENCES dept(deptid);

insert into emp values(1,'B1',2000.00,2);
insert into emp values(2,'B',2000.00,2);
insert into emp values(3,'C',1000.00,3);
insert into emp values(4,'D',2000.00,4);
insert into emp values(5,'A',1000.00,1);
insert into emp values(6,'BB1',2000.00,2);
insert into emp values(7,'BQ',2000.00,2);
insert into emp values(8,'CW',1000.00,3);
insert into emp values(9,'DE',2000.00,4);
insert into emp values(0,'AR',1000.00,1);
--
insert into emp values(12,'1B',12000.00,2);
insert into emp values(13,'2C',21000.00,3);
insert into emp values(14,'3D',32000.00,4);
insert into emp values(15,'4A',11000.00,1);



/*
Projects
ProjectID(PK)   ProjectName   ProjectBudget
1               X              1M
2               Y              2M
3               Z              3M
*/
create table projects (
    ProjectID      integer
    ,ProjectName    varchar(100)
    ,ProjectBudget   decimal(12,2)
);
-- Add Primary Key 
alter table projects add constraint pk_projects PRIMARY key (ProjectID);

insert into projects values (1,'INTERNAL1','1200000.00');
insert into projects values (2,'EXTERNAL1','5000000.00');
insert into projects values (3,'EXTERNAL2','5000000.00');



/*
EmpProjects
EP_ID(PK)      EmpID(FK)    ProjectID(FK)   StartDate  EndDate
1              1            1               jan2020     
2              1            2               mar2020
3              2            1               jan2020 
4              4            1               jan2020
5              3            1               jan2020 
6              1            2               jan2020 
7              2            3               jan2020    jan2021
*/


create table EmpProjects (
 EP_ID       integer
,EmpID       integer
,ProjectID   integer
,StartDate   date 
,EndDate     date
);

-- Add Primary Key 
alter table EmpProjects add constraint pk_EmpProjects PRIMARY key (EP_ID);
-- Add Foreign Key
ALTER TABLE EmpProjects ADD CONSTRAINT FK_ep_emp FOREIGN KEY (EmpID) REFERENCES emp(EmpID);
ALTER TABLE EmpProjects ADD CONSTRAINT FK_ep_projects FOREIGN KEY (ProjectID) REFERENCES projects(ProjectID);

delete from EmpProjects;
insert into EmpProjects values (1,1,1,to_date('21,5,2019','%d,%m,%Y'),to_date('21,5,2020','%d,%m,%Y'));
insert into EmpProjects values (2,1,2,to_date('21,5,2019','%d,%m,%Y'),to_date('21,5,2020','%d,%m,%Y'));
insert into EmpProjects values (3,2,1,to_date('21,5,2019','%d,%m,%Y'),to_date('21,5,2020','%d,%m,%Y'));
insert into EmpProjects values (4,3,1,to_date('21,5,2019','%d,%m,%Y'),to_date('21,5,2020','%d,%m,%Y'));

insert into EmpProjects values (5,4,3,to_date('21,5,2019','%d,%m,%Y'),to_date('21,5,2020','%d,%m,%Y'));
insert into EmpProjects values (6,1,3,to_date('21,5,2019','%d,%m,%Y'),to_date('21,5,2020','%d,%m,%Y'));
insert into EmpProjects values (7,1,3,to_date('21,5,2019','%d,%m,%Y'),to_date('21,5,2020','%d,%m,%Y'));
insert into EmpProjects values (8,3,2,to_date('21,5,2019','%d,%m,%Y'),to_date('21,5,2020','%d,%m,%Y'));


------------

-- Queries

-- 1. How many employees are there in my company
select * from emp;
select ename,sal from emp e;

select count(*) from emp;

select * from emp;
select 'abcd',1,empid,ename,sal,deptid from emp;

select 'Emp Sal > 1000' details, ename,sal from emp e where e.sal >1000;
select 'Emp Sal < 1000' details, ename,sal from emp e where e.sal <= 1000;


select 'Emp Sal > 1000' details, ename,sal from emp e where e.sal >1000
union
select 'Emp Sal < 1000' details, ename,sal from emp e where e.sal <= 1000;
-- intersect, minus, union - union all

select min(sal), max(sal), sum(sal)/count(*) , avg(sal) from emp;

select avg(sal) from emp;

dept  tot_sal
1     2000
2     2000
3     1000 
4     2000


------------------------------------------------------------------------------------------
select * from emp
--min(sal), max(sal), sum(sal),count(*),avg(sal) 
--group by

select deptid
       ,sum(sal) as tot_sal
       ,count(empid) as total_emps
from   emp
group  by deptid; -- unique data from teh grouped by columns


select e.ename,e.deptid ,e.sal 
from   emp e,
       (select deptid
               ,max(sal) as dept_max_sal
        from   emp
        group  by deptid) max_sal
where  e.deptid = max_sal.deptid
and    e.sal    = max_sal.dept_max_sal
--order by e.sal;
-- order by 3;
order by e.sal desc
-- order by 3 desc;


--- Update Statements
-- ----------------------------------------
select * from emp;

-- update EMP 'A's sal to 1500
update emp
set    sal   = 1500
where  ename = 'A';

-- Update the lowest salary earner in dept 2, by 1000

-- Version 1: Get all values from dept 2
select * 
from   emp
where  deptid = 2;

-- Version 2: Get min sal dept 2 with the details
select * 
from   emp
where  deptid = 2
-- ADD condition to get min sal
and    sal = (select min(sal)
              from   emp
              where  deptid = 2);
              
-- Version 3: Get min sal dept 2 with the details
select empid,ename,sal+1000 new_sal
from   emp
where  deptid = 2
-- ADD condition to get min sal
and    sal = (select min(sal)
              from   emp
              where  deptid = 2);

-- Version 4: use the subquery in update statement
update emp
set    sal = src.new_sal
from   (select empid,ename,sal+1000 new_sal
        from   emp
        where  deptid = 2
        -- ADD condition to get min sal
        and    sal = (select min(sal)
                      from   emp
                      where  deptid = 2) 
        ) src
where emp.empid = src.empid;
              
-- Check if the update is successful
select * 
from   emp
where  deptid = 2;

select * 
from   emp
where  deptid in (1, 2)
order by deptid;

-- Delete
-- delete emp BQ
delete from emp where ename = 'BQ';


select deptid, count(sal) as emps_by_dept 
from   emp
group by  deptid;


-- Cartesean Product = Matrix 
-- Cartesean Product is BAD
select  *
from    dept, emp

select  *
from    emp e, dept d
where   e.DeptID = d.DeptID

-- eliminate Cartesean product
select  *
from    emp e, dept d
where   e.DeptID = d.deptiD;

-- get the columns you need
select  d.dname
from    emp e, dept d
where   e.DeptID = d.deptiD
and     e.ename = 'A';


-- Get the matching values
select  *
from    emp, dept, projects
where   emp.DeptID = dept.DeptID
and     emp.ename = 'B'

select  EmpProjects.ep_id,emp.ename,projects.ProjectName,EmpProjects.startdate,EmpProjects.enddate
from   EmpProjects, Emp, projects
--  Base Table joins ALWAYS PK Col - FK Col 
where  EmpProjects.EmpID     = emp.empid
and    EmpProjects.ProjectID = projects.ProjectID
-- filter
and    projectname = 'EXTERNAL2'

select * from EmpProjects 

select count(1) from emp   -- 5 Rows
select count(1) from dept  -- 4 Rows
select count(1) from EmpProjects  -- 7 Rows



1   A   1000.00
2   B   2000.00
3   C   1000.00
4   D   2000.00
5   A   1000.00








select * from emp;
select * from projects;
select * from EmpProjects;

5000000
20000

Whats the total salary amount required to run ProjectID 2 for 20 months

select  sum(e.sal * 20) -- Business Rules
from    emp         e
       ,projects    p 
       ,EmpProjects ep
-- JOINS PK - FK
where  e.empid = ep.empid
and    p.projectid = ep.projectid
-- FILTERS (Join with a Value)
and    p.projectid = 1


and    ep.projectid = 2

-- Which "Dept Name" is involved with the lowest number of projects

select  count(ep.projectid),ep.projectid
from    emp         e
       ,dept        d
       ,EmpProjects ep
-- JOINS PK - FK
where  e.empid = ep.empid
and    d.deptid = e.deptid
group by ep.projectid

-- Associative Law
        select  count(ep.projectid) proj_cnt , 
                d.dname  -- , e.ename  -- , ep.projectid
        --  select ep.projectid,e.ename ,d.dname
        from    emp         e
               ,dept        d
               ,EmpProjects ep
        -- JOINS PK - FK
        where  e.empid = ep.empid
        and    d.deptid = e.deptid
        group by d.dname  -- ,e.ename
        
-- Inner Query
select src.dname
from   (
        select  count(ep.projectid) proj_cnt , d.dname
        --  select ep.projectid,e.ename ,d.dname
        from    emp         e
               ,dept        d
               ,EmpProjects ep
        -- JOINS PK - FK
        where  e.empid = ep.empid
        and    d.deptid = e.deptid
        group by d.dname ) src
where  src.proj_cnt = (     select min(min_data.cnt)
                            from   (
                                    select  count(ep.projectid) cnt
                                    --  select ep.projectid,e.ename ,d.dname
                                    from    emp         e
                                           ,dept        d
                                           ,EmpProjects ep
                                    -- JOINS PK - FK
                                    where  e.empid = ep.empid
                                    and    d.deptid = e.deptid
                                    group by d.dname ) min_data
                         );


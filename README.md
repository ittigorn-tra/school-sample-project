<!-- Output copied to clipboard! -->

<!-- Yay, no errors, warnings, or alerts! -->


# School Sample Project


## About

This is my school-student sample project built with Django and PostgreSQL for a small practice session for exploring the functionality of Django Rest Framework


## Objective

[https://manatal.notion.site/API-School-Students-Test-description-d55d5b547f344f888d904ae1c4cbef7a](https://manatal.notion.site/API-School-Students-Test-description-d55d5b547f344f888d904ae1c4cbef7a)


## Setting Up



1. Setting up python environment
    1. At project root directory, run `pipenv install`
2. Setting up a database
    2. Install postgresql on your machine
    3. For the benefit of easy development environment set up, create a database username with credential as follows:
        1. Username : ittigorn
        2. Password : password
    4. Create a database named “school_sample_project”
3. Migrate
    5. In SchoolSampleProject directory, run \
```python manage.py migrate SchoolApp```


## Models


### School


<table>
  <tr>
   <td><strong>Key</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Constraints</strong>
   </td>
  </tr>
  <tr>
   <td>school_id
   </td>
   <td>int
   </td>
   <td>Auto Increment
<p>
Primary Key
   </td>
  </tr>
  <tr>
   <td>school_name
   </td>
   <td>str
   </td>
   <td>Max length 20
   </td>
  </tr>
  <tr>
   <td>max_student
   </td>
   <td>int
   </td>
   <td>Min value 0
   </td>
  </tr>
</table>



### Student


<table>
  <tr>
   <td><strong>Key</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Constraints</strong>
   </td>
  </tr>
  <tr>
   <td>school_id
   </td>
   <td>int
   </td>
   <td>ForeignKey (School)
   </td>
  </tr>
  <tr>
   <td>student_id
   </td>
   <td>str
   </td>
   <td>Max length 20
<p>
Primary Key
   </td>
  </tr>
  <tr>
   <td>name_first
   </td>
   <td>str
   </td>
   <td>Max length 20
   </td>
  </tr>
  <tr>
   <td>name_last
   </td>
   <td>str
   </td>
   <td>Max length 20
   </td>
  </tr>
</table>



## Endpoints


### School Endpoints


#### List Schools

Path : /schools


<table>
  <tr>
   <td>Method
   </td>
   <td>
   </td>
   <td>Key
   </td>
   <td>Type
   </td>
   <td>Description
   </td>
  </tr>
  <tr>
   <td>GET
   </td>
   <td>URL Parameters
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Header
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Payload
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful HTTP status code
   </td>
   <td colspan="3" >200
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful Response
   </td>
   <td colspan="3" >



<pre class="prettyprint">[
    {
        "school_id": int,
        "school_name": str,
        "max_student": int
    },
    …
]</pre>


   </td>
  </tr>
</table>



#### List Students in School

Path : /schools/{SCHOOL_ID}/students


<table>
  <tr>
   <td>Method
   </td>
   <td>
   </td>
   <td>Key
   </td>
   <td>Type
   </td>
   <td>Description
   </td>
  </tr>
  <tr>
   <td>GET
   </td>
   <td>URL Parameters
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Header
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Payload
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful HTTP status code
   </td>
   <td colspan="3" >200
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful Response
   </td>
   <td colspan="3" >



<pre class="prettyprint">[
    {
        "school_id": int,
        "student_id": str,
        "name_first": str,
        "name_last": str
    },
    …
]</pre>


   </td>
  </tr>
</table>



#### Get School by ID

Path : /schools/{SCHOOL_ID}


<table>
  <tr>
   <td>Method
   </td>
   <td>
   </td>
   <td>Key
   </td>
   <td>Type
   </td>
   <td>Description
   </td>
  </tr>
  <tr>
   <td>GET
   </td>
   <td>URL Parameters
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Header
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Payload
   </td>
   <td colspan="3" >
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful HTTP status code
   </td>
   <td colspan="3" >200
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful Response
   </td>
   <td colspan="3" >



<pre class="prettyprint">{
    "school_id": int,
    "school_name": str,
    "max_student": int
}</pre>


   </td>
  </tr>
</table>



#### Add School

Path : /schools


<table>
  <tr>
   <td>Method
   </td>
   <td>
   </td>
   <td>Key
   </td>
   <td>Type
   </td>
   <td>Description
   </td>
  </tr>
  <tr>
   <td>POST
   </td>
   <td>URL Parameters
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Header
   </td>
   <td>Content-Type
   </td>
   <td>str
   </td>
   <td>application/json
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Payload
   </td>
   <td colspan="3" >



<pre class="prettyprint">{
    "school_id": Optional[int],
    "school_name" : str,
    "max_student" : int
}</pre>


   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful HTTP status code
   </td>
   <td colspan="3" >200
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful Response
   </td>
   <td colspan="3" >



<pre class="prettyprint">{
    "detail": "Added successfully"
}</pre>


   </td>
  </tr>
</table>



#### Update School

Path : /schools


<table>
  <tr>
   <td>Method
   </td>
   <td>
   </td>
   <td>Key
   </td>
   <td>Type
   </td>
   <td>Description
   </td>
  </tr>
  <tr>
   <td>PATCH
   </td>
   <td>URL Parameters
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Header
   </td>
   <td>Content-Type
   </td>
   <td>str
   </td>
   <td>application/json
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Payload
   </td>
   <td colspan="3" >



<pre class="prettyprint">{
    "school_id":int,
    "school_name" : Optional[str],
    "max_student" : Optional[int]
}</pre>


   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful HTTP status code
   </td>
   <td colspan="3" >200
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful Response
   </td>
   <td colspan="3" >



<pre class="prettyprint">{
    "detail": "Updated successfully"
}</pre>


   </td>
  </tr>
</table>



#### Delete School

Path : /schools/{SCHOOL_ID}


<table>
  <tr>
   <td>Method
   </td>
   <td>
   </td>
   <td>Key
   </td>
   <td>Type
   </td>
   <td>Description
   </td>
  </tr>
  <tr>
   <td>DELETE
   </td>
   <td>URL Parameters
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Header
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Payload
   </td>
   <td colspan="3" >
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful HTTP status code
   </td>
   <td colspan="3" >200
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful Response
   </td>
   <td colspan="3" >



<pre class="prettyprint">{
    "detail": "Deleted successfully"
}</pre>


   </td>
  </tr>
</table>



### Student Endpoints


#### List Students

Path : /students


<table>
  <tr>
   <td>Method
   </td>
   <td>
   </td>
   <td>Key
   </td>
   <td>Type
   </td>
   <td>Description
   </td>
  </tr>
  <tr>
   <td>GET
   </td>
   <td>URL Parameters
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Header
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Payload
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful HTTP status code
   </td>
   <td colspan="3" >200
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful Response
   </td>
   <td colspan="3" >



<pre class="prettyprint">[
    {
        "school_id": int,
        "student_id": str,
        "name_first": str,
        "name_last": str
    },
    …
]</pre>


   </td>
  </tr>
</table>



#### Get Student by ID

Path : /students/{STUDENT_ID}


<table>
  <tr>
   <td>Method
   </td>
   <td>
   </td>
   <td>Key
   </td>
   <td>Type
   </td>
   <td>Description
   </td>
  </tr>
  <tr>
   <td>GET
   </td>
   <td>URL Parameters
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Header
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Payload
   </td>
   <td colspan="3" >
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful HTTP status code
   </td>
   <td colspan="3" >200
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful Response
   </td>
   <td colspan="3" >



<pre class="prettyprint">{
    "school_id": int,
    "student_id": str,
    "name_first": str,
    "name_last": str
}</pre>


   </td>
  </tr>
</table>



#### Add Student

Path : /students


<table>
  <tr>
   <td>Method
   </td>
   <td>
   </td>
   <td>Key
   </td>
   <td>Type
   </td>
   <td>Description
   </td>
  </tr>
  <tr>
   <td>POST
   </td>
   <td>URL Parameters
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Header
   </td>
   <td>Content-Type
   </td>
   <td>str
   </td>
   <td>application/json
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Payload
   </td>
   <td colspan="3" >



<pre class="prettyprint">{
    "school_id": int,
    "student_id": str,
    "name_first": str,
    "name_last": str
}</pre>


   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful HTTP status code
   </td>
   <td colspan="3" >200
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful Response
   </td>
   <td colspan="3" >



<pre class="prettyprint">{
    "detail": "Added successfully"
}</pre>


   </td>
  </tr>
</table>



#### Update Student

Path : /students


<table>
  <tr>
   <td>Method
   </td>
   <td>
   </td>
   <td>Key
   </td>
   <td>Type
   </td>
   <td>Description
   </td>
  </tr>
  <tr>
   <td>PATCH
   </td>
   <td>URL Parameters
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Header
   </td>
   <td>Content-Type
   </td>
   <td>str
   </td>
   <td>application/json
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Payload
   </td>
   <td colspan="3" >



<pre class="prettyprint">{
    "school_id": Optional[int],
    "student_id": str,
    "name_first": Optional[str],
    "name_last": Optional[str]
}</pre>


   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful HTTP status code
   </td>
   <td colspan="3" >200
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful Response
   </td>
   <td colspan="3" >



<pre class="prettyprint">{
    "detail": "Updated successfully"
}</pre>


   </td>
  </tr>
</table>



#### Delete Student

Path : /students/{STUDENT_ID}


<table>
  <tr>
   <td>Method
   </td>
   <td>
   </td>
   <td>Key
   </td>
   <td>Type
   </td>
   <td>Description
   </td>
  </tr>
  <tr>
   <td>DELETE
   </td>
   <td>URL Parameters
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Header
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Payload
   </td>
   <td colspan="3" >
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful HTTP status code
   </td>
   <td colspan="3" >200
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Successful Response
   </td>
   <td colspan="3" >



<pre class="prettyprint">{
    "detail": "Deleted successfully"
}</pre>


   </td>
  </tr>
</table>


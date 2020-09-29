# Django + Django REST Framework Interview

This project contains the setup for a sample project which is connected to a dummy database.
The database contains dummy salaries information and its information is mapped to a middleware API that serialize this database rows in the webservice resource.

This API is implemented using Django and Django REST Framework and its only endpoint can be found here: http://localhost:8000/api/salaries

Please follow this instructions to modify the salaries endpoint

## Question 1

Modify the GET method handler of the <code>SalariesAPIView</code> view to accept a <code>name</code> parameter and lookup in the salaries table for a match in the <code>name</code> column.
For example, <code>name=AARON</code>.

## Question 2

Create a new REST API resource to insert salaries information into the <code>salaries</code> table.
To accomplish this, extend the <code>SalariesAPIView</code> to handle the POST HTTP verb and receive a payload (as shown below) and insert a new row in the salaries table.
Please note that the payload comes from a JSON object and can be serialized into a Pythonic object using <code>SalariesSerializer</code>.

Payload example:

<pre>
name: Eric Lee
position: developer
department: software
salary: $5
</pre>

## Question 3

Create a new REST API resource that allows the partial update of a single row of the salaries table.
This operations needs to be handled via the PUT HTTP verb and it must receive the <code>id</code> of the row from a URL querystring and the values to update in the data payload (in JSON format).
For example, this function needs to allow the update of the salary of a row by requesting to the URL <code>http://localhost:8000/api/salaries?id=4</code> (row with <code>id</code> equal to 4) and the following PUT payload:

<pre>
{
    "salary": "$100"
}
</pre>


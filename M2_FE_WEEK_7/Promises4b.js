const response = fetch('https://reqres.in/api/users/23',{
  headers: {
    'x-api-key': 'reqres_5364c011770343ae8b39ba3e7bcc051a',
  },
});

response.then((data) => {if (!data.ok){
      throw 'Error 404';
    }
  else {return data}})
  .then((data) => data.json()) 
  .then((data) => console.log(data["data"]))
  .catch ((error) => {
    console.log(`An error occurred: ${error}`);
  })






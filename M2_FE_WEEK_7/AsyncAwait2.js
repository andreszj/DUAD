async function getUser() {
  try {
    const response = await fetch('https://reqres.in/api/users/23',{
      headers: {
        'x-api-key': 'reqres_5364c011770343ae8b39ba3e7bcc051a',
      },
    });
    const data = await response.json();
    if (!response.ok){
      throw 'Error 404';
    }
    console.log(data ["data"])
  } catch (error) {
    console.log(`An error occurred: ${error}`);
  }
  console.log('******');
}

getUser();




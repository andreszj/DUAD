async function getUser() {
  try {
    const response = await fetch('https://reqres.in/api/users/2',{
      headers: {
        'x-api-key': 'reqres_5364c011770343ae8b39ba3e7bcc051a',
      },
    });
    const data = await response.json();
    console.log(data ["data"])
  } catch (error) {
    console.log(`An error occurred: ${error}`);
  }
  console.log('******');
}

getUser();




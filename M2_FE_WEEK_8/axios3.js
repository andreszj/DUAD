import axios from 'axios';

async function getUser(userID) {
  try {
    const response = await axios.get(`https://api.restful-api.dev/objects/${userID}`,
    {
      headers: {
        "x-api-key": "f2ee4a43-b231-4eea-991c-dc6661dd197c",
      },
    },);
  const data = response.data;
  const status = response.status;
  if (status===200) {
    await console.log(data)
  } 
  } catch (error) {
    console.log(`An error occurred: ${error}`);
    }
}


getUser("ff8081819d82fab6019d9924fa461d71")

getUser("ff8081819d82fab6019d9ll924fa461d71")
import axios from 'axios';

async function getUserAndModify(userID,newAddress) {
  try {
    const response = await axios.get(`https://api.restful-api.dev/objects/${userID}`,
    {
      headers: {
        "x-api-key": "f2ee4a43-b231-4eea-991c-dc6661dd197c",
      },
    },);
  const data = await response.data;
  const status = await response.status;
  if (status ===200) {
    console.log("Data Imported:",data)
    data.data["address"] =newAddress;
    console.log("Modified Data:",data)
    const putResponse = await axios.put(`https://api.restful-api.dev/objects/${userID}`, data, {
      headers: {
        "x-api-key": "f2ee4a43-b231-4eea-991c-dc6661dd197c",
      },
    },)

  } else {
    throw "Error 404";
    }
  } catch (error) {
    console.log(`An error occurred: ${error}`);
    }
}


// getUserAndModify("ff8081819d82fab6019d9924fa461d71","Nicaragua")

getUserAndModify("ff8081819d82fab6019d9924fa461d71","Costa Nica")
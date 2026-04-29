async function getUserAndModify(userID,newAddress) {
  try {
    const response = await fetch(`https://api.restful-api.dev/objects/${userID}`,{
      headers: {
        "x-api-key": "f2ee4a43-b231-4eea-991c-dc6661dd197c",
      },
    },);
  const data = await response.json();
  const status = await response.status;
  if (response.ok) {
    console.log("Data Imported:",data)
    data.data["address"] =newAddress;
    console.log("Modified Data:",data)
    const puResponse = await fetch(`https://api.restful-api.dev/objects/${userID}`, {
      method: "PUT",
      headers: {
          "x-api-key": "f2ee4a43-b231-4eea-991c-dc6661dd197c",
          "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
  } else {
    throw "Error 404";
    }
  } catch (error) {
    console.log(`An error occurred: ${error}`);
    }
}


getUserAndModify("ff8081819d82fab6019d9924fa461d71","Nicaragua")

getUserAndModify("ff8081819d82fab6019d9924fa461d71","Peru")
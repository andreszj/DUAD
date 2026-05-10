import axios from 'axios';

const getData = async () => {
	console.log("Loading data...");
	const response = await axios.get(`https://api.restful-api.dev/objects`);
	console.log("Data loaded! Returning...");
	return response.data;
}

const data = await getData();
console.log(data);

for (const item of data) {
    if (item.data != null) {

        let details = "";

        for (const key in item.data) {
            details += `${key}: ${item.data[key]}, `;
        }
        details = details.slice(0, -2); //se investiga para esta funcion

        const objectAPI = `${item.name} (${details})`;
        console.log(objectAPI)
    }
}
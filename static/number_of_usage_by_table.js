fetch("/api/number_of_usage_by_table")
  .then((res) => res.json())
  .then((data) => {
    console.log("customerData", data);
  });

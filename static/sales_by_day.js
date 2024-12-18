fetch("/api/sales_by_day")
  .then((res) => res.json())
  .then((data) => {
    console.log("sales_by_day", data);
  });

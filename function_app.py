import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger1", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("triggered")

    country = req.params.get("country")
    city = req.params.get("city")
    if not country or not city:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            city = req_body.get("city")
            country = req_body.get("country")
    if country and city:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "please provide a city or country as parameters or in the body",
             status_code=200
        )
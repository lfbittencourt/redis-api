# Redis API

This is a simple API example using [Flask](http://flask.pocoo.org/) and
[Redis](https://redis.io/).

## Requisites

- [Docker](https://www.docker.com/) or
[Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/)

## How to run it

It's dead simple: type `docker-compose up`, wait for it to complete and hit some
of the endpoints listed below.

Note that the hostname may change depending on how you installed Docker. If you
have installed Docker Toolbox (in case you're running Windows 10 **Home**, for
example), hostname will be the IP returned by `docker-machine ip` command,
otherwise it will be "localhost".

The port remains the same (5000) no matter which installation you have made.

## Endpoints

### `POST /cart/<CART_ID>`

Creates a cart. No body required. Example response:

```json
[]
```

### `POST /cart/<CART_ID>/products`

Adds a product to the cart. Example post body:

```json
{
    "product_id": 456
}
```

Example response:

```json
[
    123,
    456
]
```

### `GET /cart/<CART_ID>`

Gets the cart. Example response:

```json
[
    123,
    456
]
```

### `DELETE /cart/<CART_ID>/products/<PRODUCT_ID>`

Deletes product from the cart. Example response:

```json
[
    456
]
```

### `DELETE /cart/<CART_ID>`

Deletes the cart. Example response:

```json
true
```

## Postman collection

You can easily test all endpoints importing `postman_collection.json` in
Postman. Hostname (including port) is isolated in a variable, so you can change
it for all requests if needed.

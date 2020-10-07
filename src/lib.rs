#[macro_use]
extern crate serde;

#[derive(Deserialize, Serialize)]
pub struct TT {
    s: String,
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}

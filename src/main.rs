#[macro_use]
extern crate serde;

/// test
#[derive(Deserialize, Serialize)]
pub struct TT {
    s: String,
}

fn main() {
    println!("Hello World!");
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}

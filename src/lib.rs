
/// test
pub struct TT {
    s: String,
}

struct Unused;

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}

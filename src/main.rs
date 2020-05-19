use std::env;

fn main() {
    let mut args = env::args().skip(1);

    let prog = args.next().expect("jq program");
    let input = args.next().expect("data input");

    match jq_rs::run(&prog, &input) {
        Ok(s) => println!("{}", s),
        Err(e) => eprintln!("{}", e),
    }
}

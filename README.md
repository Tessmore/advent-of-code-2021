# Advent of code-2021

* Code for https://adventofcode.com/


## Rust

* Initialize new project:

```
cargo new day01 --bin
```

* Running/building:

```
cargo run
```


#### TIL

Debug printing

```
println!("{:?}", tmp);
```

---

Splitting text/strings: https://stackoverflow.com/a/38138985

```
s.lines()
s.split_whitespace()
s.split("separator")  |  s.split('/')  |  s.split(char::is_numeric)
```

---

Map ([https://doc.rust-lang.org/std/iter/struct.Map.html](https://doc.rust-lang.org/std/iter/struct.Map.html))

```
.map(| input | output)

.map(| input | { with a function })
```

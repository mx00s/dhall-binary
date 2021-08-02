\(bs : ./Type) ->
  let bytes =
        (../Prelude).Text.concatMap
          ../B1/Type
          (\(b : ../B1/Type) -> if b then "1" else "0")
          bs

  in  "b'${bytes}'"

let toBitString
    : ./Type -> ../BitString/Type
    = \(b : ./Type) ->
        (../Prelude).List.concat
          ../B1/Type
          [ ../B64/toBitString b._1, ../B64/toBitString b._2 ]

in  toBitString

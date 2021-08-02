let toBitString
    : ./Type -> ../BitString/Type
    = \(b : ./Type) ->
        (../Prelude).List.concat
          ../B1/Type
          [ ../B32/toBitString b._1, ../B32/toBitString b._2 ]

in  toBitString

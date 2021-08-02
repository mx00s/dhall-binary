let toBitString
    : ./Type -> ../BitString/Type
    = \(b : ./Type) ->
        (../Prelude).List.concat
          ../B1/Type
          [ ../B8/toBitString b._1, ../B8/toBitString b._2 ]

in  toBitString

let toBitString
    : ./Type -> ../BitString/Type
    = \(b : ./Type) -> if b then [ True ] else [ False ]

in  toBitString

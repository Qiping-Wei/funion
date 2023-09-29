solidity_pool_path = "C:\\Users\\18178\\collected_contracts\\SmartContractDataset-main\\"
temp_path="C:\\Users\\18178\\PycharmProjects\\funion\\temp\\"
result_path="C:\\Users\\18178\\collected_contracts\\SmartContractDataset_processed\\"

# add contract pools that are used in the contracts in the solidity pool
openzeppelin_path='C:\\Users\\18178\\collected_contracts\\openzeppelin\\'
chainlink_path='C:\\Users\\18178\\collected_contracts\\chainlink\\'
uniswap_path='C:\\Users\\18178\\collected_contracts\\uniswap\\'

contract_pool_name_path_map={
    "uniswap":uniswap_path,
    "chainlink":chainlink_path,
    "openzeppelin":openzeppelin_path,
}

# for individual Solidity files
file_index=0
parameters=[
    [
        'C:\\Users\\18178\\collected_contracts\\SmartContractDataset-main\\SmartContractDataset-main\\gambling_contracts\\',
        'Roulette.sol'
    ],
    # a case that import file import another file with the name.
    [
        'C:\\Users\\18178\collected_contracts\\SmartContractDataset-main\\soliditySourceCodes\\nft-bonanza\\',
        'BonanzaMarketplace.sol'
    ]
    ,
    [
        'C:\\Users\\18178\\collected_contracts\\SmartContractDataset-main\\soliditySourceCodes\\fatality\\',
        'AutoCompoundVault.sol'
    ],
    # # SolcError: DeclarationError: Undeclared identifier.
    # # Math is not declared.
    [
        'C:\\Users\\18178\collected_contracts\\SmartContractDataset-main\\SmartContractDataset-main\\soliditySourceCodes\\game-assets\\',
        'GameAsset.sol'
    ],
    # SolcError: DeclarationError: Identifier not found or not unique.
    # one import file have Context. another import file has its own Context.
    [
        'C:\\Users\\18178\\collected_contracts\\SmartContractDataset-main\\SmartContractDataset-main\\soliditySourceCodes\\bonding-curve\\',
        'EminenceCurrency.sol'
    ]
]
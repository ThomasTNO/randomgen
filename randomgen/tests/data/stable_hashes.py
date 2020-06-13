known_hashes = {
    ("ChaCha", "seed"): {
        "random_values": "0dda65c819197b3ca467f053869aa1f4a4123cb2e55a290453651916dd7002bd",
        "initial_state_hash": "1ded27d6bb53619c8b6d5decfac0e50bae731c6c962b7dafdb89c5ca941e631d",
        "final_state_hash": "9042f89dd26a7fc4c8f23ba841b61c7d7cf3a53ded37d0a61709da7b3c131ff7",
    },
    ("ChaCha", "key"): {
        "random_values": "cf07b4d5286923c2fb4318d5a985b9ba29aac59f7eb5be7ef0395c76cb5a8e71",
        "initial_state_hash": "8cc40691e74bcdef396b947c94bdb56bc965662c54afccd9da286f30842e7e4d",
        "final_state_hash": "45ecbbcc4a9b6cb1e39d90c3d0f87958ef9fcfb87574e454656745fe2c7f993b",
    },
    ("ChaCha", "seed", "counter"): {
        "random_values": "bc6eb9280caf3ebacdd7fe4632213320671774af919d310c1e5529b4dea62202",
        "initial_state_hash": "3c4127efbde9495984ecf84f5e7de6408a3b6f9e085cd16e5553320c19dc9b35",
        "final_state_hash": "e2f11faef5c70ca32a67763f307651c94162647c10aff3b3c3323c921342daa5",
    },
    ("ChaCha", "counter", "key"): {
        "random_values": "8e773b7ff72ef03fe692bd7e9fcfd0b03830d430309204e1319ed4033c9b4f2d",
        "initial_state_hash": "1e2d43ed43dbebbe9fb0dc0ab6c1d4a9e4004dac5d95340a9e0f039f64b1f4b7",
        "final_state_hash": "291e79b08b208006138169258eae8b4ab30c900b767e9f36b2885e6de4554d60",
    },
    ("Xoroshiro128", "seed"): {
        "random_values": "3ff37d80a806de5f21fb31d05897caa5e59a186d7aca1b81efc5c1ba53cfa64b",
        "initial_state_hash": "df6e73b6bc302d13b9309adef7fb207cc5e294e88883712f4b64b9c817a962f4",
        "final_state_hash": "6f706ac8c3d50298d34e0211983cee4b5bf1c41f9bc3f31374195736c595c6e9",
    },
    ("Xoroshiro128", "seed", "plusplus", True): {
        "random_values": "8b659c6525a6a050ad91c327d27817bb95dda54af3fc21de27756c2bcf2d96cb",
        "initial_state_hash": "bff56c72d4e8d24187658b8d51b178061a0a189c5f26afb6132069900e462f73",
        "final_state_hash": "087b5f13e4ef2171c5b4215aea56bbb68af23db7e0832da3f4be67506efa9a03",
    },
    ("Xoroshiro128", "seed", "plusplus", False): {
        "random_values": "3ff37d80a806de5f21fb31d05897caa5e59a186d7aca1b81efc5c1ba53cfa64b",
        "initial_state_hash": "df6e73b6bc302d13b9309adef7fb207cc5e294e88883712f4b64b9c817a962f4",
        "final_state_hash": "6f706ac8c3d50298d34e0211983cee4b5bf1c41f9bc3f31374195736c595c6e9",
    },
    ("Xorshift1024", "seed"): {
        "random_values": "1512c88b31d595bf768dd5cd5ba516a8df4a3ddfbe7251267418e861ccd1eeae",
        "initial_state_hash": "6e31fb7fe4c3abf1a136014d973b33f06f188d0f1444467279e1ed7d9954d149",
        "final_state_hash": "ca9d8ca020ad0dbbc731256a04ad50368506a5487ed62244494283da9ba723f6",
    },
    ("Xoshiro256", "seed"): {
        "random_values": "67b529922570a33ee50716624e38b4b098e2bbf18f18e4f0361805409a5d2038",
        "initial_state_hash": "fcee5f7c91d6ec387736c7281d2c2a99db21fa093fceec153b0e588ae4346540",
        "final_state_hash": "9d4caf0acb1c4eb990fe8dc91db6a38b663f7255fe0be95f5f62e577488e6410",
    },
    ("Xoshiro512", "seed"): {
        "random_values": "462d5ed83a4e6f4373291884858b66eced70b3377cabe01029ff62abfaf5d157",
        "initial_state_hash": "d2610c1fda0815d51dba75bc0f2cd627b42b418915753df477c008abb7b7ceb1",
        "final_state_hash": "0150dbdde7145328375ef9f93bbd6239dfcee15c68247d84520dc88543a217a2",
    },
    ("LXM", "seed"): {
        "random_values": "c98015d91fe08823720c58803ed790230c6d1a499367cf101d934890063da35c",
        "initial_state_hash": "627e7dcc2cef199787f262fae45ecf73a7561a0e236e7ac84db7b55a20e4f343",
        "final_state_hash": "da5473e62d244c4808cefd3818d98cb11a7e6fe65ac4bbbb7a323612abd75cb4",
    },
    ("LXM", "seed", "mix", True): {
        "random_values": "c98015d91fe08823720c58803ed790230c6d1a499367cf101d934890063da35c",
        "initial_state_hash": "627e7dcc2cef199787f262fae45ecf73a7561a0e236e7ac84db7b55a20e4f343",
        "final_state_hash": "da5473e62d244c4808cefd3818d98cb11a7e6fe65ac4bbbb7a323612abd75cb4",
    },
    ("LXM", "seed", "mix", False): {
        "random_values": "b63a8d75a689d604a4578f7e11521c05f1b88c52454cf23cdae455e95aa077d0",
        "initial_state_hash": "627e7dcc2cef199787f262fae45ecf73a7561a0e236e7ac84db7b55a20e4f343",
        "final_state_hash": "da5473e62d244c4808cefd3818d98cb11a7e6fe65ac4bbbb7a323612abd75cb4",
    },
    ("MT64", "seed"): {
        "random_values": "9c10fe3d07af95ee3c01e47802704f56c66d5d4fe80df09de9ada20da14c364c",
        "initial_state_hash": "00065ceea3c768fe4242085e5a3fc428c9f00e7bd32e5a213bfd9976271d23b2",
        "final_state_hash": "4b365cb9948e87b3892a9783c2769b7f03b4da223659e3bc63f77779ff0caa2c",
    },
    ("MT19937", "seed"): {
        "random_values": "de6797f1e0209e9a3afb9cdbe52fb524fb7fb23416e2a0aa92625319d3b4f7e8",
        "initial_state_hash": "567c1b44adca76c5c52d86fbfae48b3482b3fb6f3daa70538dd92e2d064e6317",
        "final_state_hash": "d9f8ad8a2e45cfd7ad762ce595894e804e9a0c6d27bc15070308e84a12479792",
    },
    ("DSFMT", "seed"): {
        "random_values": "d758b303c4b920998fc51510ad47e2e3e07da050cd994d47b3c5bf724749452c",
        "initial_state_hash": "e548dee51d75909e0efc0be13bcbda261819f27a32ac3570288c4693a5a8f1bf",
        "final_state_hash": "abc45003a8f310a45bd1a0e20b94932635614f7fb9b7754b796355bc8cea6f51",
    },
    ("SFC64", "seed"): {
        "random_values": "a74ce7f815c8e47a191d2710c6ec882a1b8ef84ae45217be353434693f802d7c",
        "initial_state_hash": "2b59e5d1f70e235c15a22fc029a206c2a5d3d0dce77c32463e4305d06022ccce",
        "final_state_hash": "9361e056dece1c9d752755b9e228ef7f145354fbbe3b80b924ba562f35a42ee9",
    },
    ("SFC64", "seed", "k", 1): {
        "random_values": "a74ce7f815c8e47a191d2710c6ec882a1b8ef84ae45217be353434693f802d7c",
        "initial_state_hash": "2b59e5d1f70e235c15a22fc029a206c2a5d3d0dce77c32463e4305d06022ccce",
        "final_state_hash": "9361e056dece1c9d752755b9e228ef7f145354fbbe3b80b924ba562f35a42ee9",
    },
    ("SFC64", "seed", "k", 10998731014437268875): {
        "random_values": "d1f90196160e1ffabd66857e4ac9f6ea8679b18600ac55fa77dffe6e2fce914f",
        "initial_state_hash": "737c98b18f6335b74d686685985eeb10f8a18f70606f6dcc3e4f006e0d3e58fc",
        "final_state_hash": "f15e8b25ff504bdfc5430b3a6630a8df3bce41d507fa075311150934da24a56c",
    },
    ("SFMT", "seed"): {
        "random_values": "57a9772542955f750bc5e08946712b14b7efdb0e0d9dd6ca9015db02b0feb5c2",
        "initial_state_hash": "3f630040e74c93760d66d4b550cdd83b65d6ff48b5bad368a9698e502fe113bd",
        "final_state_hash": "e4f78633f2782616099b9b07e20d8d8dde1ecf6a6f9f9136dfe208a8d29565b0",
    },
    ("SPECK128", "seed"): {
        "random_values": "d0a22bd5875d5c4c2262b51f06237307eb1e8b7627377c97868ce7d8d8e4f636",
        "initial_state_hash": "df6b8e5c64c036d440c7bf2574c9d898e5693d2022d6b6991d3821773c8cf1d0",
        "final_state_hash": "40029ea2116f45130388f3bdb37ed9bf12a06c7acd61a3d42e5c50c0a3f38819",
    },
    ("SPECK128", "key"): {
        "random_values": "bbba46e041a0a3b930fde1aba620a91e524d07dd3f02da94f26ecd8cd304362e",
        "initial_state_hash": "14bf2299554d57500bd8962439202a736ba79e130bd8e18d7890d18b3f55ef33",
        "final_state_hash": "2b82db1eaf2de29dfa3ed91e91a10bc05c5f57d35e0412db71b317674341d868",
    },
    ("SPECK128", "seed", "counter"): {
        "random_values": "52a5b231552b3f41b5dec43b0319aec730e89963e02a3fc154c3ddaa554085ad",
        "initial_state_hash": "2f7cae1c97125dcc846df57fae9ada86519e211d3c4259bf28473cb89285539f",
        "final_state_hash": "ecc5fefecd45b7df7917f1af3582b0e9452ba855e193f3249e97be1b02727c18",
    },
    ("SPECK128", "counter", "key"): {
        "random_values": "7a608f5e3292d6598728016cd143ec01f9fdc16b8d08824953f8c463c1e28f95",
        "initial_state_hash": "7730f500ce39885dcc24c69123763d083361f42a50aead3e5093186160900ba5",
        "final_state_hash": "78826431a76ffc95f68af869cbd38bd35be8fd7c08e43a8761110d72fba73b22",
    },
    ("PCG32", "seed"): {
        "random_values": "961142eb8786582f48a942bec78e8b059c7e0feed6019638ec804d2a0ad7e23f",
        "initial_state_hash": "246358a9ecc83746473c8be8d25de59e4426be050c553f71b76fc17c6f2448d4",
        "final_state_hash": "ce7621b9f707df3f2b9b42c324e532634703ea16ad6421f632030166f6df97fd",
    },
    ("PCG32", "seed", "inc"): {
        "random_values": "03d397920cbdccc03ebc5b6a49fdf749150a08a4e36ddd2f0cf4557b48338b7f",
        "initial_state_hash": "e4388eae288c344c78ad47cdbfe0983778d75b56c117cbb16ffdd0efc68d61aa",
        "final_state_hash": "d1b7623dfdb1084149c34472f63f65b2ae59b5013c5e72d47160597a0fe855a4",
    },
    ("PCG64", "seed"): {
        "random_values": "4d8bbff64c61c5f3158a043946b78d9c556091df421baf1dd5fbd506d7610dd2",
        "initial_state_hash": "52424eb4d0f3518635c0d36a93637c39a9d2b8f949f6dd5d737ca9b83610c3da",
        "final_state_hash": "6e7714d72766dc092faa6d2bf841aa8e8eae8530834d3eb5324b949d1740fd85",
    },
    ("PCG64", "seed", "inc"): {
        "random_values": "63fd3334317fb8902e5fdc9baf11b01ed5d098b3cdb7333e0da529edb8e09ae0",
        "initial_state_hash": "f2c4eba60d5c1dc2818987ad19994cce76fdfa1fc2680e3bd3be2012e32fd0d4",
        "final_state_hash": "e93bed1d80626ae63762c5d64ab099e321c838beaa7ee24006ad50981a0a65ed",
    },
    ("PCG64", "seed", "variant", "xsl-rr"): {
        "random_values": "4d8bbff64c61c5f3158a043946b78d9c556091df421baf1dd5fbd506d7610dd2",
        "initial_state_hash": "52424eb4d0f3518635c0d36a93637c39a9d2b8f949f6dd5d737ca9b83610c3da",
        "final_state_hash": "6e7714d72766dc092faa6d2bf841aa8e8eae8530834d3eb5324b949d1740fd85",
    },
    ("PCG64", "seed", "variant", "dxsm"): {
        "random_values": "007aaf954de7435d87abe06fb957cbade21732c6ceafb80335e89a5ca322440e",
        "initial_state_hash": "52424eb4d0f3518635c0d36a93637c39a9d2b8f949f6dd5d737ca9b83610c3da",
        "final_state_hash": "6e7714d72766dc092faa6d2bf841aa8e8eae8530834d3eb5324b949d1740fd85",
    },
    ("PCG64", "seed", "variant", "cm-dxsm"): {
        "random_values": "4b984c9ab74ab3473895b0ff4f782826f8c86b8e92e57c198440794153facf9f",
        "initial_state_hash": "3e093b9322aae9f40219284443010226a068fb2b6f42d41e83a9ee2f992c9886",
        "final_state_hash": "1aa7f247ad9245d611276469125b2b0dc25b3aed3d9ab6158a439efe0cb9155a",
    },
    ("PCG64", "seed", "inc", "variant", "xsl-rr"): {
        "random_values": "63fd3334317fb8902e5fdc9baf11b01ed5d098b3cdb7333e0da529edb8e09ae0",
        "initial_state_hash": "f2c4eba60d5c1dc2818987ad19994cce76fdfa1fc2680e3bd3be2012e32fd0d4",
        "final_state_hash": "e93bed1d80626ae63762c5d64ab099e321c838beaa7ee24006ad50981a0a65ed",
    },
    ("PCG64", "seed", "inc", "variant", "dxsm"): {
        "random_values": "88539e900241b39371085897fc069e0582ff4529876fba2f4c15d9861d0fed9b",
        "initial_state_hash": "f2c4eba60d5c1dc2818987ad19994cce76fdfa1fc2680e3bd3be2012e32fd0d4",
        "final_state_hash": "e93bed1d80626ae63762c5d64ab099e321c838beaa7ee24006ad50981a0a65ed",
    },
    ("PCG64", "seed", "inc", "variant", "cm-dxsm"): {
        "random_values": "eb406352a02f182cc65c5443d028e6ddd7af9260d6fccb9edda7b824d009e1df",
        "initial_state_hash": "73cf476d2aeb333f5f81a1095c2fba66f4e42223e4f32a36390aa83c91104b1e",
        "final_state_hash": "9cd88b41a398af2d2a98d1c0cdafce1181c42cbd0ca3e8ed2595d5b17733d217",
    },
    ("AESCounter", "seed"): {
        "random_values": "475b8b4363e7aee8bd5022f1a2a0a5a125ca701a3c7585396cc0c7bdfb56c35e",
        "initial_state_hash": "9437a0c633aac707ee481628600ced2f179aa0c02a6e60540cab412e4b80c22e",
        "final_state_hash": "e5006b5d9bb180b16c6dcb947126ad0431ec1433a2b42cab263fcaacd69400e6",
    },
    ("AESCounter", "key"): {
        "random_values": "a67bb222cd34bc6669fabcef696dcb59962b99f02c8d6f2973b2b7198c7b4f6e",
        "initial_state_hash": "3f010da816b9fb73c4302a7ae08ec827630408a646dfa154d332eaa54fc86831",
        "final_state_hash": "2bda54055d16f380b340b6afbdd934176d22c22ac02c3338f4124f200c07e90d",
    },
    ("AESCounter", "seed", "counter"): {
        "random_values": "90706c2682cfc6ddd5d7dd445b6e7d7576f637cc2893fe9223b84589291efa0a",
        "initial_state_hash": "896f63d51a7d1fbc58efcf3716eae3ab10f2d8b99d49e665dfe8dc7f4b4c5aa5",
        "final_state_hash": "4ee6b74e9f458a2f816113b998ce1c3c0635444e84b459f6e1d160cb3beae18f",
    },
    ("AESCounter", "key", "counter"): {
        "random_values": "db466f69593fddef03efdfa936b725025d671b7a007146feaae14db9f3ae590e",
        "initial_state_hash": "f575d8515d21c9849e37fa3655ce941737f8ed68da53577a1e677952ef85b55e",
        "final_state_hash": "7843875db631ba602965b95ee408b2f914182c5d5336c9c12dd55718649c53f9",
    },
    ("HC128", "seed"): {
        "random_values": "31d3cd1019ad913858bcdb1767fdf070c60db1b2610e017a522b27c1ae55adaf",
        "initial_state_hash": "555b19837a44f89419c2ec968bd17899d960d8252739011698238c99c0124cbd",
        "final_state_hash": "d1e9b91945af353faffbec551688c8a606532b4a46f47abad0317cf85967c2dd",
    },
    ("JSF", "seed"): {
        "random_values": "6fb1be3b54be2e910ec1ad90101032780fef8b1d0f8b0065c05829567975d786",
        "initial_state_hash": "aadae0048e97430c8cc0b272620ec2a9ed5d5457a9ca5f41d61e60965a24f762",
        "final_state_hash": "98ad1efe9a5c540be047ef19ef4ec3113aea624385b51a6959c0b0499c469090",
    },
    ("JSF", "seed", "seed_size", 1): {
        "random_values": "6fb1be3b54be2e910ec1ad90101032780fef8b1d0f8b0065c05829567975d786",
        "initial_state_hash": "aadae0048e97430c8cc0b272620ec2a9ed5d5457a9ca5f41d61e60965a24f762",
        "final_state_hash": "98ad1efe9a5c540be047ef19ef4ec3113aea624385b51a6959c0b0499c469090",
    },
    ("JSF", "seed", "seed_size", 2): {
        "random_values": "44d82d54c1d4840d40b4f51e1a35e4d5d6f345222ff1be50e1aa2164b2d8cfe8",
        "initial_state_hash": "1c124788e80ca278afd3ba068ae1eb8b8ce8d3c55822c82a73d5a5720a4a6e6c",
        "final_state_hash": "03280857814a09da19685b22ed26a0cd16c424ab627de1607e2355689bd966ee",
    },
    ("JSF", "seed", "seed_size", 3): {
        "random_values": "ee40c817d05a4ea5e73ccfe02512b57a315daa6ca1f51cd141caaf75d5c5b9fb",
        "initial_state_hash": "89a590e2a453adc9561cc3de594e1f8f88041929a5fcc002467608367f0787e8",
        "final_state_hash": "b80526f95c48cbd5e77f0eff469866d3c4cc205bb07ae84a11ab8e0d6971a818",
    },
    ("JSF", "seed", "size", 32): {
        "random_values": "f77eea980fa123f6c5d4f23d54361e606fc0d947f5e95fa27867399980b903cf",
        "initial_state_hash": "55ca1e564961dffa3b614e388dcaa5764b80ede2f30cefb2064195517ac2c545",
        "final_state_hash": "6dffd72526a0d74834de9985c074dd50cc7f0b9b4fb5beac21e46a5979e7e700",
    },
    ("JSF", "seed", "size", 64): {
        "random_values": "6fb1be3b54be2e910ec1ad90101032780fef8b1d0f8b0065c05829567975d786",
        "initial_state_hash": "aadae0048e97430c8cc0b272620ec2a9ed5d5457a9ca5f41d61e60965a24f762",
        "final_state_hash": "98ad1efe9a5c540be047ef19ef4ec3113aea624385b51a6959c0b0499c469090",
    },
    ("JSF", "seed", "seed_size", 1, "size", 32): {
        "random_values": "f77eea980fa123f6c5d4f23d54361e606fc0d947f5e95fa27867399980b903cf",
        "initial_state_hash": "55ca1e564961dffa3b614e388dcaa5764b80ede2f30cefb2064195517ac2c545",
        "final_state_hash": "6dffd72526a0d74834de9985c074dd50cc7f0b9b4fb5beac21e46a5979e7e700",
    },
    ("JSF", "seed", "seed_size", 1, "size", 64): {
        "random_values": "6fb1be3b54be2e910ec1ad90101032780fef8b1d0f8b0065c05829567975d786",
        "initial_state_hash": "aadae0048e97430c8cc0b272620ec2a9ed5d5457a9ca5f41d61e60965a24f762",
        "final_state_hash": "98ad1efe9a5c540be047ef19ef4ec3113aea624385b51a6959c0b0499c469090",
    },
    ("JSF", "seed", "seed_size", 2, "size", 32): {
        "random_values": "bc2a4a226808516518c05ca5571bd07253d9d041cf8fc979ffeda8d53f2e2b00",
        "initial_state_hash": "884ed1107874f5c8cb4246bd57cd5435818108cc275017e3a86727fc9f5474ca",
        "final_state_hash": "3ccd6ed0705cc4bd5dc4b51048074015f658e9488dd642869dfda7b925be30cb",
    },
    ("JSF", "seed", "seed_size", 2, "size", 64): {
        "random_values": "44d82d54c1d4840d40b4f51e1a35e4d5d6f345222ff1be50e1aa2164b2d8cfe8",
        "initial_state_hash": "1c124788e80ca278afd3ba068ae1eb8b8ce8d3c55822c82a73d5a5720a4a6e6c",
        "final_state_hash": "03280857814a09da19685b22ed26a0cd16c424ab627de1607e2355689bd966ee",
    },
    ("JSF", "seed", "seed_size", 3, "size", 32): {
        "random_values": "0ea49782e3a1b0761a56b1da457a630644411e799d12a29de503b2cc3782cef4",
        "initial_state_hash": "3612dff91c0d9598af8304262159f0cd99c27284ab262c918c364e785e0e9571",
        "final_state_hash": "438c75f396d5275c400ea1d4746e10b7f705090b55572825913b8c3c12447c7e",
    },
    ("JSF", "seed", "seed_size", 3, "size", 64): {
        "random_values": "ee40c817d05a4ea5e73ccfe02512b57a315daa6ca1f51cd141caaf75d5c5b9fb",
        "initial_state_hash": "89a590e2a453adc9561cc3de594e1f8f88041929a5fcc002467608367f0787e8",
        "final_state_hash": "b80526f95c48cbd5e77f0eff469866d3c4cc205bb07ae84a11ab8e0d6971a818",
    },
    ("Philox", "seed"): {
        "random_values": "bc90bdc019d1c5bac6bec53ca831379627592b0831b80b59e4afb263c5ce11fd",
        "initial_state_hash": "80a4e83e9540bb7547e6a401a7942cb30c1fd73bacaf77baf0010b29ca0a578a",
        "final_state_hash": "5868f28299a738042bcac4fd46b314eeb5b889b3f12bd84471b21580181921d1",
    },
    ("Philox", "key"): {
        "random_values": "12db7bf022e0ab25a38e4cf0e42db3602a51f80d18012ee5db05701491bb9d00",
        "initial_state_hash": "7466821b8b6d5f2f34f8b72213f32095c1d6c56d3e3babd33fa270169c0ad7eb",
        "final_state_hash": "88217a239b6b789a17b7f556667c9ffa899d38ac29baabf24827939ee0b6f9b1",
    },
    ("Philox", "seed", "number", 2): {
        "random_values": "48e9b87b6f3dedcc0dea64d819a3769f2d359af7ed3d8c0e012ee00ebc0d61f4",
        "initial_state_hash": "c1a1ab5e19973c6a768ccfef9e0d64058bc1997590f85d9d6f577c219d450c0d",
        "final_state_hash": "71a07d2cda5c0167a6cfc585c7e34370d147db44addd02d773bd0d1edc39371d",
    },
    ("Philox", "seed", "number", 4): {
        "random_values": "bc90bdc019d1c5bac6bec53ca831379627592b0831b80b59e4afb263c5ce11fd",
        "initial_state_hash": "80a4e83e9540bb7547e6a401a7942cb30c1fd73bacaf77baf0010b29ca0a578a",
        "final_state_hash": "5868f28299a738042bcac4fd46b314eeb5b889b3f12bd84471b21580181921d1",
    },
    ("Philox", "seed", "width", 32): {
        "random_values": "33a57973b963d2c79ede4dfdc636a2ff89f5a681e9548ddc6480607072b4bcde",
        "initial_state_hash": "2a86f154591791b8446e28a64dcf01b20df944c6f49a9d8038550fdf1b5a28b0",
        "final_state_hash": "ed5b472234979f25564be35e1459bcb8fc7059f7f30841e09736c149db942a5e",
    },
    ("Philox", "seed", "width", 64): {
        "random_values": "bc90bdc019d1c5bac6bec53ca831379627592b0831b80b59e4afb263c5ce11fd",
        "initial_state_hash": "80a4e83e9540bb7547e6a401a7942cb30c1fd73bacaf77baf0010b29ca0a578a",
        "final_state_hash": "5868f28299a738042bcac4fd46b314eeb5b889b3f12bd84471b21580181921d1",
    },
    ("Philox", "seed", "counter"): {
        "random_values": "20a8bffba45fb1e050e32dd65b19b6fca62b979c0452a23de872c479f2fe9e0c",
        "initial_state_hash": "3a9b9c7583b4f85f63da01bfe21c6978af7bb68a94f301f11e942a6d747fd392",
        "final_state_hash": "a82bfd633a603a8477a0db790e2fb719d1cc8598faf7e3771d03b6b9610ec1c6",
    },
    ("Philox", "key", "number", 2): {
        "random_values": "2c77f61cb1d1c804d06d78918d6c8614ca2c1237f30b9950afcf6a58b74432eb",
        "initial_state_hash": "d553b187c399a244971d0f038e204980fe8d9263cf35dc46760c6f1cde9612c3",
        "final_state_hash": "fa6aaf49997620e6e61a494c9a04c28f4ac0b2eeefa2c6d42caf9a524a528a34",
    },
    ("Philox", "key", "number", 4): {
        "random_values": "12db7bf022e0ab25a38e4cf0e42db3602a51f80d18012ee5db05701491bb9d00",
        "initial_state_hash": "7466821b8b6d5f2f34f8b72213f32095c1d6c56d3e3babd33fa270169c0ad7eb",
        "final_state_hash": "88217a239b6b789a17b7f556667c9ffa899d38ac29baabf24827939ee0b6f9b1",
    },
    ("Philox", "key", "width", 32): {
        "random_values": "370f7144658347110312b81b8fd91f650dcdbfcb72ced92899956e8d71653fd4",
        "initial_state_hash": "641302affae90ef993e7d84a3208664cc82ebd61f6e7913dbc8f2c0a7a4fa262",
        "final_state_hash": "4c6c26e4b376e6b3028bc50de4dd45a05b7586f1a5ced5fe1e9fa05d66bd9c66",
    },
    ("Philox", "key", "width", 64): {
        "random_values": "12db7bf022e0ab25a38e4cf0e42db3602a51f80d18012ee5db05701491bb9d00",
        "initial_state_hash": "7466821b8b6d5f2f34f8b72213f32095c1d6c56d3e3babd33fa270169c0ad7eb",
        "final_state_hash": "88217a239b6b789a17b7f556667c9ffa899d38ac29baabf24827939ee0b6f9b1",
    },
    ("Philox", "counter", "key"): {
        "random_values": "2d5252bfa2ef7d025757bed026eda0dfb771ceacb7c43e738f64e557e51b1fa3",
        "initial_state_hash": "18d238f9d0a154027cdbd76d13e73d0bb8b5ab3954f832b43e533f6167038ff7",
        "final_state_hash": "b30abf205c56e50ee2bf51867139502b71c3b183a3069dbc7dcf939b74530b4d",
    },
    ("Philox", "seed", "number", 2, "width", 32): {
        "random_values": "e584623a8441d6ef640d757f444f827124f9712ac5b9d5185e48ce0dbfd6a82a",
        "initial_state_hash": "5b3658ad76127a56ee1eafa279f29040fa5f4e2cadb73b9f3c7a07202d210002",
        "final_state_hash": "4a3b8bbd885bf9567ec64a59377e447892e00ba6df87cde2e2df36402509abe2",
    },
    ("Philox", "seed", "number", 2, "width", 64): {
        "random_values": "48e9b87b6f3dedcc0dea64d819a3769f2d359af7ed3d8c0e012ee00ebc0d61f4",
        "initial_state_hash": "c1a1ab5e19973c6a768ccfef9e0d64058bc1997590f85d9d6f577c219d450c0d",
        "final_state_hash": "71a07d2cda5c0167a6cfc585c7e34370d147db44addd02d773bd0d1edc39371d",
    },
    ("Philox", "seed", "number", 4, "width", 32): {
        "random_values": "33a57973b963d2c79ede4dfdc636a2ff89f5a681e9548ddc6480607072b4bcde",
        "initial_state_hash": "2a86f154591791b8446e28a64dcf01b20df944c6f49a9d8038550fdf1b5a28b0",
        "final_state_hash": "ed5b472234979f25564be35e1459bcb8fc7059f7f30841e09736c149db942a5e",
    },
    ("Philox", "seed", "number", 4, "width", 64): {
        "random_values": "bc90bdc019d1c5bac6bec53ca831379627592b0831b80b59e4afb263c5ce11fd",
        "initial_state_hash": "80a4e83e9540bb7547e6a401a7942cb30c1fd73bacaf77baf0010b29ca0a578a",
        "final_state_hash": "5868f28299a738042bcac4fd46b314eeb5b889b3f12bd84471b21580181921d1",
    },
    ("Philox", "seed", "counter", "number", 2): {
        "random_values": "770e71df438e88a4caecc5e1136f06b375eb9360bd2d3edb3888b2daf1bdbf41",
        "initial_state_hash": "c5c9758eb5724637ee730e69d9c17bda32584fe7f8b36a3b38cc89b20c502129",
        "final_state_hash": "466ff805c6d61d48c5570ca9148ed7fedbfdc85cd2715548672c0df058f0937c",
    },
    ("Philox", "seed", "counter", "number", 4): {
        "random_values": "20a8bffba45fb1e050e32dd65b19b6fca62b979c0452a23de872c479f2fe9e0c",
        "initial_state_hash": "3a9b9c7583b4f85f63da01bfe21c6978af7bb68a94f301f11e942a6d747fd392",
        "final_state_hash": "a82bfd633a603a8477a0db790e2fb719d1cc8598faf7e3771d03b6b9610ec1c6",
    },
    ("Philox", "seed", "counter", "width", 32): {
        "random_values": "6a542bd74cd64d0edd390505df5438d3d5dce6fb26842803e8742a876cf699b8",
        "initial_state_hash": "a4df88d0d778fdb136b14bb717721a053145b720f61e212cb6357a903fdac73b",
        "final_state_hash": "c06d00f8136ea84229d66a8f07d14fbb687888603d2ac907676208eb4d7ecc6e",
    },
    ("Philox", "seed", "counter", "width", 64): {
        "random_values": "20a8bffba45fb1e050e32dd65b19b6fca62b979c0452a23de872c479f2fe9e0c",
        "initial_state_hash": "3a9b9c7583b4f85f63da01bfe21c6978af7bb68a94f301f11e942a6d747fd392",
        "final_state_hash": "a82bfd633a603a8477a0db790e2fb719d1cc8598faf7e3771d03b6b9610ec1c6",
    },
    ("Philox", "key", "number", 2, "width", 32): {
        "random_values": "fd75f7908fe6226864714fa239ba21e36cd9a420c849f075ebbf513b42f54336",
        "initial_state_hash": "701835d6659b42fac78722d6088b47eee40def27e52d55cb8241c2873d28ca74",
        "final_state_hash": "1ac88c123d1f487bea8108ad71e17e65a3f4f29d1574ca7e88914d629d0ccd2e",
    },
    ("Philox", "key", "number", 2, "width", 64): {
        "random_values": "2c77f61cb1d1c804d06d78918d6c8614ca2c1237f30b9950afcf6a58b74432eb",
        "initial_state_hash": "d553b187c399a244971d0f038e204980fe8d9263cf35dc46760c6f1cde9612c3",
        "final_state_hash": "fa6aaf49997620e6e61a494c9a04c28f4ac0b2eeefa2c6d42caf9a524a528a34",
    },
    ("Philox", "key", "number", 4, "width", 32): {
        "random_values": "370f7144658347110312b81b8fd91f650dcdbfcb72ced92899956e8d71653fd4",
        "initial_state_hash": "641302affae90ef993e7d84a3208664cc82ebd61f6e7913dbc8f2c0a7a4fa262",
        "final_state_hash": "4c6c26e4b376e6b3028bc50de4dd45a05b7586f1a5ced5fe1e9fa05d66bd9c66",
    },
    ("Philox", "key", "number", 4, "width", 64): {
        "random_values": "12db7bf022e0ab25a38e4cf0e42db3602a51f80d18012ee5db05701491bb9d00",
        "initial_state_hash": "7466821b8b6d5f2f34f8b72213f32095c1d6c56d3e3babd33fa270169c0ad7eb",
        "final_state_hash": "88217a239b6b789a17b7f556667c9ffa899d38ac29baabf24827939ee0b6f9b1",
    },
    ("Philox", "counter", "key", "number", 2): {
        "random_values": "e2ee5c58e58b7684de3791a3d925023d4b281602d2880b7a6594cf46e0e0974e",
        "initial_state_hash": "ed563bcd9f5f23d9bef85ab4011776ddbe4bbd183d9d72af52e971db117344e1",
        "final_state_hash": "87bc572655b66536941b2e9758699cc178aead492bdb3a02f0d28f8cbbce9a11",
    },
    ("Philox", "counter", "key", "number", 4): {
        "random_values": "2d5252bfa2ef7d025757bed026eda0dfb771ceacb7c43e738f64e557e51b1fa3",
        "initial_state_hash": "18d238f9d0a154027cdbd76d13e73d0bb8b5ab3954f832b43e533f6167038ff7",
        "final_state_hash": "b30abf205c56e50ee2bf51867139502b71c3b183a3069dbc7dcf939b74530b4d",
    },
    ("Philox", "counter", "key", "width", 32): {
        "random_values": "b95b97b641dcd4998a4b341b6f19add14e02e5aae9f8dc3b5013d90b0e4853e6",
        "initial_state_hash": "a32a6ae7a1400895db623afd2a4dc5495bd3fe8a4f3129b94f97d676033ca0fe",
        "final_state_hash": "25016f737ce340563b21bb239b5705a4b014ea8bf5e2cba628190ab97a08c43c",
    },
    ("Philox", "counter", "key", "width", 64): {
        "random_values": "2d5252bfa2ef7d025757bed026eda0dfb771ceacb7c43e738f64e557e51b1fa3",
        "initial_state_hash": "18d238f9d0a154027cdbd76d13e73d0bb8b5ab3954f832b43e533f6167038ff7",
        "final_state_hash": "b30abf205c56e50ee2bf51867139502b71c3b183a3069dbc7dcf939b74530b4d",
    },
    ("Philox", "seed", "counter", "number", 2, "width", 32): {
        "random_values": "8f02206bc4e20a4d6f0e0b74382a65269edb62ba390cdf716330f1f7d2c53a1b",
        "initial_state_hash": "4c4dfc8d90cae7bf04828a1743ae9e4e1126eebc1b87492d6e0a0d127c1ed4cd",
        "final_state_hash": "eebf842111e0535e75a5741db9da27b6011a5d4d926e059689c888a0aac3be3c",
    },
    ("Philox", "seed", "counter", "number", 2, "width", 64): {
        "random_values": "770e71df438e88a4caecc5e1136f06b375eb9360bd2d3edb3888b2daf1bdbf41",
        "initial_state_hash": "c5c9758eb5724637ee730e69d9c17bda32584fe7f8b36a3b38cc89b20c502129",
        "final_state_hash": "466ff805c6d61d48c5570ca9148ed7fedbfdc85cd2715548672c0df058f0937c",
    },
    ("Philox", "seed", "counter", "number", 4, "width", 32): {
        "random_values": "6a542bd74cd64d0edd390505df5438d3d5dce6fb26842803e8742a876cf699b8",
        "initial_state_hash": "a4df88d0d778fdb136b14bb717721a053145b720f61e212cb6357a903fdac73b",
        "final_state_hash": "c06d00f8136ea84229d66a8f07d14fbb687888603d2ac907676208eb4d7ecc6e",
    },
    ("Philox", "seed", "counter", "number", 4, "width", 64): {
        "random_values": "20a8bffba45fb1e050e32dd65b19b6fca62b979c0452a23de872c479f2fe9e0c",
        "initial_state_hash": "3a9b9c7583b4f85f63da01bfe21c6978af7bb68a94f301f11e942a6d747fd392",
        "final_state_hash": "a82bfd633a603a8477a0db790e2fb719d1cc8598faf7e3771d03b6b9610ec1c6",
    },
    ("Philox", "counter", "key", "number", 2, "width", 32): {
        "random_values": "4b52ff53a5a9816b7c4021c3f5c67624cd391539af94b71bf0d5d3772e600aa6",
        "initial_state_hash": "fad53459156760542ee7329eb5cbe5a2e0b51e040243c449bff1243105a8f792",
        "final_state_hash": "4600b81e9a0ff2a3f7b2c3e8a1dd399d2a2f60f2ed0e35d2e0d09bd5f12fb89f",
    },
    ("Philox", "counter", "key", "number", 2, "width", 64): {
        "random_values": "e2ee5c58e58b7684de3791a3d925023d4b281602d2880b7a6594cf46e0e0974e",
        "initial_state_hash": "ed563bcd9f5f23d9bef85ab4011776ddbe4bbd183d9d72af52e971db117344e1",
        "final_state_hash": "87bc572655b66536941b2e9758699cc178aead492bdb3a02f0d28f8cbbce9a11",
    },
    ("Philox", "counter", "key", "number", 4, "width", 32): {
        "random_values": "b95b97b641dcd4998a4b341b6f19add14e02e5aae9f8dc3b5013d90b0e4853e6",
        "initial_state_hash": "a32a6ae7a1400895db623afd2a4dc5495bd3fe8a4f3129b94f97d676033ca0fe",
        "final_state_hash": "25016f737ce340563b21bb239b5705a4b014ea8bf5e2cba628190ab97a08c43c",
    },
    ("Philox", "counter", "key", "number", 4, "width", 64): {
        "random_values": "2d5252bfa2ef7d025757bed026eda0dfb771ceacb7c43e738f64e557e51b1fa3",
        "initial_state_hash": "18d238f9d0a154027cdbd76d13e73d0bb8b5ab3954f832b43e533f6167038ff7",
        "final_state_hash": "b30abf205c56e50ee2bf51867139502b71c3b183a3069dbc7dcf939b74530b4d",
    },
    ("ThreeFry", "seed"): {
        "random_values": "6a0ce1a57c1d7fdc91efcc519176b7f8fb7553d684ff07038a659862fbb877e9",
        "initial_state_hash": "f0f91d48d6dadb538169345970a6f46004ee595c046d49a2db77e58b4316266f",
        "final_state_hash": "376ad91cb1ce1fe490cf1a700b3c7706659103b0610346bff9c761951b6464a7",
    },
    ("ThreeFry", "key"): {
        "random_values": "a8ea53a7e3a559890a91356fc31ae879f30a3ea88baf14f7997faa8a23894457",
        "initial_state_hash": "51c870ae8af7d9d4f82501d5533662a76663684bc573d1ee046949ac055a0614",
        "final_state_hash": "9a7f91cd8f8385315d8890118c3c185fe0a111dfcaccea518c00d1d8c0212678",
    },
    ("ThreeFry", "seed", "number", 2): {
        "random_values": "5cf840b4f12d5bcbee80fa0fb01969b13421923bbf06eb69c5417f01ea14365b",
        "initial_state_hash": "ca05529bc8b669c0bf9667f281e0dd4967ff6876319c6ef4ea9414d8b58c240a",
        "final_state_hash": "15833429c3659702831ec5b2533888cad8d215de728f528e66158621e493a1e3",
    },
    ("ThreeFry", "seed", "number", 4): {
        "random_values": "6a0ce1a57c1d7fdc91efcc519176b7f8fb7553d684ff07038a659862fbb877e9",
        "initial_state_hash": "f0f91d48d6dadb538169345970a6f46004ee595c046d49a2db77e58b4316266f",
        "final_state_hash": "376ad91cb1ce1fe490cf1a700b3c7706659103b0610346bff9c761951b6464a7",
    },
    ("ThreeFry", "seed", "width", 32): {
        "random_values": "04933a58593c142d9b9acd8d3e220b44b45f68ca4e756e5c305bdace792e0d2f",
        "initial_state_hash": "d0dcadfe9c9be5a0761c2077d12a5bb0e4b49f2696e6f969256b76ff726334d7",
        "final_state_hash": "5a1232c35fe3b752eac49b596360674eed8bdc16d7feb160a0009b0542d97460",
    },
    ("ThreeFry", "seed", "width", 64): {
        "random_values": "6a0ce1a57c1d7fdc91efcc519176b7f8fb7553d684ff07038a659862fbb877e9",
        "initial_state_hash": "f0f91d48d6dadb538169345970a6f46004ee595c046d49a2db77e58b4316266f",
        "final_state_hash": "376ad91cb1ce1fe490cf1a700b3c7706659103b0610346bff9c761951b6464a7",
    },
    ("ThreeFry", "seed", "counter"): {
        "random_values": "c6f1520b128c4af38bf3d94ea0644364da3d10686392f1636bf069a6b8da2735",
        "initial_state_hash": "0714052e2a4b0f251ff7c56ae3ad3beb7c46c3d6c2c0d6f414bd3189166c0e2c",
        "final_state_hash": "835a0c68335b6abe639ef876a65d691f7721f8aeb7cd58b0cfbbfcb4a18ee7dd",
    },
    ("ThreeFry", "key", "number", 2): {
        "random_values": "33cbaedfe895ec6fe5349b2f90ae3adda09e349f33bdc02121644a6558221603",
        "initial_state_hash": "c13d3698e83190a150c839e2ca051a03ce9d7c5dcecfafec817258fccd3428ab",
        "final_state_hash": "0d5408f6db2f636d7e8e0e69ee74e9b9041df6a54b88ab0a6d13628b32c119aa",
    },
    ("ThreeFry", "key", "number", 4): {
        "random_values": "a8ea53a7e3a559890a91356fc31ae879f30a3ea88baf14f7997faa8a23894457",
        "initial_state_hash": "51c870ae8af7d9d4f82501d5533662a76663684bc573d1ee046949ac055a0614",
        "final_state_hash": "9a7f91cd8f8385315d8890118c3c185fe0a111dfcaccea518c00d1d8c0212678",
    },
    ("ThreeFry", "key", "width", 32): {
        "random_values": "2ba849e210f225b6ff5ce29e44149e5e7e0cc97bd0199d713259479305104adc",
        "initial_state_hash": "cde5190a5f37f731dc2e2cc56d2752347baa4b7ae3eeedae4c43749e80e75e76",
        "final_state_hash": "f9c7cda95978115fc037da0e18f2c230ea1f3c4ec295a65415d7678e89d4afae",
    },
    ("ThreeFry", "key", "width", 64): {
        "random_values": "a8ea53a7e3a559890a91356fc31ae879f30a3ea88baf14f7997faa8a23894457",
        "initial_state_hash": "51c870ae8af7d9d4f82501d5533662a76663684bc573d1ee046949ac055a0614",
        "final_state_hash": "9a7f91cd8f8385315d8890118c3c185fe0a111dfcaccea518c00d1d8c0212678",
    },
    ("ThreeFry", "counter", "key"): {
        "random_values": "25b866f7ea1c07c038a7c9171600818aa56f301eba78b78b99e18f12e63be3c3",
        "initial_state_hash": "35ebc819d8f1aa7221351102db3262f93da7aebd1792989299ca925d7888d500",
        "final_state_hash": "c3853500044108dd8456aed82bd5943f06e471e45e3150dfc7fc30bc29d15f22",
    },
    ("ThreeFry", "seed", "number", 2, "width", 32): {
        "random_values": "a4864e23a19857ec1f9e01c190d9173c1c6f015ae8420754870b64fb0dd26bc9",
        "initial_state_hash": "639665313caaff0c82ea0bf3ebe52e9a21a4fc89f06f02dceb72ea8bd452769a",
        "final_state_hash": "695a381f4bb2b72eaa269e4afd1d1b67593b6a57bd8958b5437950aa645db6be",
    },
    ("ThreeFry", "seed", "number", 2, "width", 64): {
        "random_values": "5cf840b4f12d5bcbee80fa0fb01969b13421923bbf06eb69c5417f01ea14365b",
        "initial_state_hash": "ca05529bc8b669c0bf9667f281e0dd4967ff6876319c6ef4ea9414d8b58c240a",
        "final_state_hash": "15833429c3659702831ec5b2533888cad8d215de728f528e66158621e493a1e3",
    },
    ("ThreeFry", "seed", "number", 4, "width", 32): {
        "random_values": "04933a58593c142d9b9acd8d3e220b44b45f68ca4e756e5c305bdace792e0d2f",
        "initial_state_hash": "d0dcadfe9c9be5a0761c2077d12a5bb0e4b49f2696e6f969256b76ff726334d7",
        "final_state_hash": "5a1232c35fe3b752eac49b596360674eed8bdc16d7feb160a0009b0542d97460",
    },
    ("ThreeFry", "seed", "number", 4, "width", 64): {
        "random_values": "6a0ce1a57c1d7fdc91efcc519176b7f8fb7553d684ff07038a659862fbb877e9",
        "initial_state_hash": "f0f91d48d6dadb538169345970a6f46004ee595c046d49a2db77e58b4316266f",
        "final_state_hash": "376ad91cb1ce1fe490cf1a700b3c7706659103b0610346bff9c761951b6464a7",
    },
    ("ThreeFry", "seed", "counter", "number", 2): {
        "random_values": "c6bf820bad3fc39ac51b7da69cee0a0a9be74fbfdcf717231f8ec0035ab73620",
        "initial_state_hash": "16ace6c74ced7812784102dd425ec7098310cef687531be32bd6ba99d8b4b157",
        "final_state_hash": "81417ef1c7c7592880d4fd602dc18a0770cb6c3ef619aa281767763e209bdd3c",
    },
    ("ThreeFry", "seed", "counter", "number", 4): {
        "random_values": "c6f1520b128c4af38bf3d94ea0644364da3d10686392f1636bf069a6b8da2735",
        "initial_state_hash": "0714052e2a4b0f251ff7c56ae3ad3beb7c46c3d6c2c0d6f414bd3189166c0e2c",
        "final_state_hash": "835a0c68335b6abe639ef876a65d691f7721f8aeb7cd58b0cfbbfcb4a18ee7dd",
    },
    ("ThreeFry", "seed", "counter", "width", 32): {
        "random_values": "764e93381248f0ff0f440460cceff9ae1ac1bbacba3619490684b620c8265b77",
        "initial_state_hash": "5f484f75d99abccde0c0537e6a819d477a5eca99ff72acc0f29a5dc720ab43a6",
        "final_state_hash": "bf60489059f7ca20b96905dea911d6192e53d3fcab526e1d8d6865e46d96a6fb",
    },
    ("ThreeFry", "seed", "counter", "width", 64): {
        "random_values": "c6f1520b128c4af38bf3d94ea0644364da3d10686392f1636bf069a6b8da2735",
        "initial_state_hash": "0714052e2a4b0f251ff7c56ae3ad3beb7c46c3d6c2c0d6f414bd3189166c0e2c",
        "final_state_hash": "835a0c68335b6abe639ef876a65d691f7721f8aeb7cd58b0cfbbfcb4a18ee7dd",
    },
    ("ThreeFry", "key", "number", 2, "width", 32): {
        "random_values": "c757a77a4c2dc6710cac3c2b031e4d832fb6862fd1d744fff95d7baef78f6c3e",
        "initial_state_hash": "c1156bf9439f6666e54833cbeeecd13a462020c22770c46d1b7cd1839e0df7f6",
        "final_state_hash": "ca884a9957a6ecd897c73fdb75468fc86b5c50c8c01b27bc5deaa8dde342d009",
    },
    ("ThreeFry", "key", "number", 2, "width", 64): {
        "random_values": "33cbaedfe895ec6fe5349b2f90ae3adda09e349f33bdc02121644a6558221603",
        "initial_state_hash": "c13d3698e83190a150c839e2ca051a03ce9d7c5dcecfafec817258fccd3428ab",
        "final_state_hash": "0d5408f6db2f636d7e8e0e69ee74e9b9041df6a54b88ab0a6d13628b32c119aa",
    },
    ("ThreeFry", "key", "number", 4, "width", 32): {
        "random_values": "2ba849e210f225b6ff5ce29e44149e5e7e0cc97bd0199d713259479305104adc",
        "initial_state_hash": "cde5190a5f37f731dc2e2cc56d2752347baa4b7ae3eeedae4c43749e80e75e76",
        "final_state_hash": "f9c7cda95978115fc037da0e18f2c230ea1f3c4ec295a65415d7678e89d4afae",
    },
    ("ThreeFry", "key", "number", 4, "width", 64): {
        "random_values": "a8ea53a7e3a559890a91356fc31ae879f30a3ea88baf14f7997faa8a23894457",
        "initial_state_hash": "51c870ae8af7d9d4f82501d5533662a76663684bc573d1ee046949ac055a0614",
        "final_state_hash": "9a7f91cd8f8385315d8890118c3c185fe0a111dfcaccea518c00d1d8c0212678",
    },
    ("ThreeFry", "counter", "key", "number", 2): {
        "random_values": "0fb5d5f947d1d66624ae4b20bf3948b3fbe5cf3678d7e5dd2ecdb11312859bc2",
        "initial_state_hash": "12aff453f5102defd050e2692a7b7b9d37e46a0c7792d4b75a863c622729f9d6",
        "final_state_hash": "0091b2d2a2903d5a3e84c1bf0a1e85b99ba6dfc236b216c2c1481c92cd43654c",
    },
    ("ThreeFry", "counter", "key", "number", 4): {
        "random_values": "25b866f7ea1c07c038a7c9171600818aa56f301eba78b78b99e18f12e63be3c3",
        "initial_state_hash": "35ebc819d8f1aa7221351102db3262f93da7aebd1792989299ca925d7888d500",
        "final_state_hash": "c3853500044108dd8456aed82bd5943f06e471e45e3150dfc7fc30bc29d15f22",
    },
    ("ThreeFry", "counter", "key", "width", 32): {
        "random_values": "f80b442b0be3b37c27fe45beae10ead34adb3f8da63af4277911c2d13b24a6c7",
        "initial_state_hash": "b6f06c796d7708cdb5ba711085f5329d271ea2bd0d1687299e8a88cdb880ed62",
        "final_state_hash": "aa063347bb419f06ba4b15ea15133f831bc708c2264f72b4df6dfd80a9c58730",
    },
    ("ThreeFry", "counter", "key", "width", 64): {
        "random_values": "25b866f7ea1c07c038a7c9171600818aa56f301eba78b78b99e18f12e63be3c3",
        "initial_state_hash": "35ebc819d8f1aa7221351102db3262f93da7aebd1792989299ca925d7888d500",
        "final_state_hash": "c3853500044108dd8456aed82bd5943f06e471e45e3150dfc7fc30bc29d15f22",
    },
    ("ThreeFry", "seed", "counter", "number", 2, "width", 32): {
        "random_values": "7ab2f3577b70421764dea0c632b977e6baa359a3245b9fcc62b0a881f22babf8",
        "initial_state_hash": "74353087895949f5a1656e0f5bd4945be457923001b5fca85c176867908ca8be",
        "final_state_hash": "af9938c92c22dbededff008467caaf3e8498eddcb1c1d7510425c1f62d952c53",
    },
    ("ThreeFry", "seed", "counter", "number", 2, "width", 64): {
        "random_values": "c6bf820bad3fc39ac51b7da69cee0a0a9be74fbfdcf717231f8ec0035ab73620",
        "initial_state_hash": "16ace6c74ced7812784102dd425ec7098310cef687531be32bd6ba99d8b4b157",
        "final_state_hash": "81417ef1c7c7592880d4fd602dc18a0770cb6c3ef619aa281767763e209bdd3c",
    },
    ("ThreeFry", "seed", "counter", "number", 4, "width", 32): {
        "random_values": "764e93381248f0ff0f440460cceff9ae1ac1bbacba3619490684b620c8265b77",
        "initial_state_hash": "5f484f75d99abccde0c0537e6a819d477a5eca99ff72acc0f29a5dc720ab43a6",
        "final_state_hash": "bf60489059f7ca20b96905dea911d6192e53d3fcab526e1d8d6865e46d96a6fb",
    },
    ("ThreeFry", "seed", "counter", "number", 4, "width", 64): {
        "random_values": "c6f1520b128c4af38bf3d94ea0644364da3d10686392f1636bf069a6b8da2735",
        "initial_state_hash": "0714052e2a4b0f251ff7c56ae3ad3beb7c46c3d6c2c0d6f414bd3189166c0e2c",
        "final_state_hash": "835a0c68335b6abe639ef876a65d691f7721f8aeb7cd58b0cfbbfcb4a18ee7dd",
    },
    ("ThreeFry", "counter", "key", "number", 2, "width", 32): {
        "random_values": "1c092eeb065ee79faeb4608402b65cbc00242c643aceb504b581302618d59348",
        "initial_state_hash": "d0b3027100b86eb962e9d56c5c8ee73f16bdd0cf3a0b3c0299d123c80d34f5d0",
        "final_state_hash": "b58005f649bf563a007a995e22609e60232bd05c302e281b1e0a1cbde019ae74",
    },
    ("ThreeFry", "counter", "key", "number", 2, "width", 64): {
        "random_values": "0fb5d5f947d1d66624ae4b20bf3948b3fbe5cf3678d7e5dd2ecdb11312859bc2",
        "initial_state_hash": "12aff453f5102defd050e2692a7b7b9d37e46a0c7792d4b75a863c622729f9d6",
        "final_state_hash": "0091b2d2a2903d5a3e84c1bf0a1e85b99ba6dfc236b216c2c1481c92cd43654c",
    },
    ("ThreeFry", "counter", "key", "number", 4, "width", 32): {
        "random_values": "f80b442b0be3b37c27fe45beae10ead34adb3f8da63af4277911c2d13b24a6c7",
        "initial_state_hash": "b6f06c796d7708cdb5ba711085f5329d271ea2bd0d1687299e8a88cdb880ed62",
        "final_state_hash": "aa063347bb419f06ba4b15ea15133f831bc708c2264f72b4df6dfd80a9c58730",
    },
    ("ThreeFry", "counter", "key", "number", 4, "width", 64): {
        "random_values": "25b866f7ea1c07c038a7c9171600818aa56f301eba78b78b99e18f12e63be3c3",
        "initial_state_hash": "35ebc819d8f1aa7221351102db3262f93da7aebd1792989299ca925d7888d500",
        "final_state_hash": "c3853500044108dd8456aed82bd5943f06e471e45e3150dfc7fc30bc29d15f22",
    },
}

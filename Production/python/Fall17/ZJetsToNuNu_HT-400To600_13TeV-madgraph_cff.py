import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/002E07F0-445B-E811-A047-000101000936.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/025EEFFA-425B-E811-A8F7-001E673D0C31.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/14A5314A-535B-E811-A2B6-000101000961.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/180439F2-365B-E811-9CFC-001E67F8FA2E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/18AB5807-425B-E811-96EF-001E6739AC59.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/22E86CE9-8C5A-E811-B64E-000101000923.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/2621E202-395B-E811-90E4-00010100092F.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/2C432065-255B-E811-9F7D-000101000963.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/32BE9C85-345B-E811-AB2D-00010100096E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/3AD68057-455B-E811-B0A2-001E67F8F6F0.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/4AF3D298-485B-E811-929C-000101000974.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/68E9E6F0-9B5A-E811-9DDA-FA163E4C57FA.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/70DBE202-395B-E811-A527-00010100092F.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/7E39BEF5-8B5A-E811-9439-FA163E501CAF.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/84867537-A45A-E811-8F34-00010100097E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/8C8132C6-4A5B-E811-A241-000101000963.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/907937AC-405B-E811-BF36-00010100092E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/96A88D53-3B5B-E811-A002-00010100092E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/CA2DDC45-285B-E811-AC2F-001E6739C8B9.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/CC137B7F-355B-E811-A801-00010100092F.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/F461CEAA-CD5A-E811-A598-000101000968.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/FA478944-B05A-E811-B7DD-00010100096E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/025C3FD2-365B-E811-8AA7-000101000935.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/165AC901-205B-E811-A318-000101000962.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/1C82C1B1-585B-E811-A983-000101000920.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/20B9DF9C-1E5B-E811-818D-000101000934.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/443920FB-6B5C-E811-A7FE-000101000927.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/4E299EFD-1F5B-E811-8763-00010100096E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/5ACDAF04-205B-E811-BE80-000101000963.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/6269EC2B-405B-E811-A51C-000101000977.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/705CB844-375B-E811-BF6E-001E6739B7D9.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/72D70728-3C5B-E811-9FAA-9CB65404FBA0.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/741D7CEF-265B-E811-898B-001E67F8FA4C.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/80D3BB1B-495B-E811-A1C0-000101000963.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/9A23B2C9-265B-E811-A490-001E6739ABB9.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/9A38B78C-495B-E811-AB4B-000101000964.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/A82A825D-445B-E811-97AF-00010100097C.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/B6F69C9F-215B-E811-8011-000101000963.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/BAE3A6E6-395B-E811-BF15-00010100092E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/C20E1F7F-285B-E811-8739-000101000965.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/C4A2FF05-355B-E811-AB81-000101000962.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/CAB22498-215B-E811-9C07-001E673CFA89.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/CE6FB4DA-245B-E811-A994-000101000927.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/DA852DEF-3D5B-E811-9777-000101000926.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/DE040413-525B-E811-BE7D-000101000978.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/E8207880-225B-E811-8262-001E673D0079.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/EC0875B9-465B-E811-B5FB-001E6739AB19.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/EC2987D5-245B-E811-B931-00010100097A.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/F602765C-445B-E811-9C1A-00010100092C.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/F66568FE-385B-E811-BEEC-000101000927.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/0272193F-61A1-E811-9707-0CC47A7FC682.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/0E170E50-28A1-E811-969A-3417EBE7051F.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/12886315-4DA1-E811-9F18-002590DD7E50.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/1412BEDE-83A1-E811-A8A6-3417EBE706C3.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/14F88407-90A1-E811-A708-002590DE6DD4.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/1CCE1810-16A1-E811-B829-002590DE3A92.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/1EF80713-11A1-E811-996F-002590DE6E34.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/20A68998-6DA1-E811-B492-0CC47A7E6972.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/281D464A-6CA1-E811-8CD7-F04DA274CA01.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/2E018585-99A1-E811-8903-3417EBE7446B.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/3056087F-66A1-E811-909D-3417EBE70069.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/30CC9A4C-95A1-E811-8A55-00266CF3E248.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/342B1683-62A1-E811-9218-0CC47A7E6A4C.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/44EFDF6E-42A1-E811-8823-002590DE6E1E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/56575485-5BA1-E811-AE57-0CC47A7FC74A.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/5A5ADA77-86A1-E811-830C-003048C4E818.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/5AAD34FE-57A1-E811-8AA5-0CC47A7E6A74.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/5EEE732D-54A1-E811-B900-3417EBE700A2.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/607DE579-32A1-E811-AB6F-F04DA2751915.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/62A9EC98-7EA1-E811-B7FB-3417EBE7047A.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/62F58B5D-56A1-E811-B0B9-40F2E9C6B036.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/705B7F34-8BA1-E811-A7F4-40F2E9C6B000.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/706D219D-5FA1-E811-A2EA-3417EBE74303.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/729EC670-86A1-E811-8231-002590DE6E28.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/7ADF1263-22A1-E811-B893-002590DE6E1E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/7C28F081-62A1-E811-8DBF-002590DE6E28.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/8CAF2369-6AA1-E811-A7B2-40F2E9C6AF2E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/8E087100-44A1-E811-A288-00266CF3E164.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/9CBD093F-72A1-E811-9013-F04DA274CA01.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/9E0AA277-39A1-E811-8AE0-3417EBE70078.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/A47B4967-76A1-E811-9819-0CC47A4DB6CC.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/A81976BC-7FA1-E811-B614-002590DE6DE4.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/A8A5DD9D-50A1-E811-AA52-3417EBE70729.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/A8EFAD73-3DA1-E811-A93C-002590DE6E34.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/B01AEEF3-7BA1-E811-8AAD-3417EBE7047A.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/CCC61ECB-88A1-E811-BF73-003048C4E81C.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D465EC5F-75A1-E811-931C-002590DE38C8.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D66EFDB0-49A1-E811-A869-0CC47A7FC72C.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/E628A7AD-2EA1-E811-A9DF-F04DA2751915.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/EECBABB4-1DA1-E811-B1CB-F04DA274CA22.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/F0E54A6B-6AA1-E811-89A3-F04DA274BC29.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/F22D309D-6DA1-E811-9C6B-3417EBE705EB.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/F445851E-4BA1-E811-808E-3417EBE7446B.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/FAAA1CB6-6FA1-E811-A15E-F04DA274BC29.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/FE6326C3-91A1-E811-A445-3417EBE6FFFD.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/FEEA986B-77A1-E811-85A3-0CC47AC33AB2.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/008E7829-108F-E811-A6CF-02163E01A95A.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/0A340DDF-E38E-E811-990A-0242AC1C0501.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/1247D400-218F-E811-B294-FA163EBBC4FC.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/1463C125-D88E-E811-87B0-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/1AC395E9-E38E-E811-B3DF-0242AC1C0501.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/1EDEC15E-508F-E811-8A17-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/2AA4CD0E-DC8E-E811-A8D4-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/30EC3EE3-E38E-E811-88C7-0242AC1C0501.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/3AE2426A-B88E-E811-BD84-FA163E4B46ED.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/482C7394-148F-E811-B8EB-02163E01A95A.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/56BAE7A9-CB8E-E811-8559-0242AC1C0505.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/5C2664EE-E88E-E811-B200-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/64EF28CF-178F-E811-84D1-FA163E4E857F.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/6C156642-4D8F-E811-AE5C-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/829C7D8D-1B8F-E811-AA55-FA163EB5C28E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/86CA25AC-138F-E811-9B30-FA163E056F1C.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/8A3411B9-CB8E-E811-8F18-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/9AF0E5A1-0A8F-E811-B383-FA163E9A0B63.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/B48CF6EB-DB8E-E811-8B90-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/E2B9BB3A-4E8F-E811-9026-FA163E9AE434.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/E2C4EE6D-0F8F-E811-B0C6-FA163EAE3931.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/F0EA123A-D78E-E811-A564-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/08B4BBC7-AD5A-E811-9092-44A84225C629.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/209D3A65-3A5B-E811-8833-000101000929.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/2E5F0B06-355B-E811-856B-000101000962.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/32ECB7CC-265B-E811-8165-001E67F8F9CA.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/60EE12DA-245B-E811-9B91-000101000923.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/6C53BE40-1F5B-E811-9C65-000101000926.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/7005C826-295B-E811-BBCD-001E6739B019.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/88484784-5A5B-E811-BCB8-00010100097F.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/940C1518-425B-E811-A2BB-000101000963.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/A24F5C9C-985B-E811-8C94-000101000972.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/A69CF262-A55A-E811-8864-00010100092D.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/AE13D8D7-255B-E811-BED2-000101000923.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/C03D4144-375B-E811-A1AF-001E673CFA89.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/06475BA4-405B-E811-99DC-001E673D0041.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/0E04A26D-395B-E811-810E-001E673CFA89.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/3A38D06B-395B-E811-B061-001E673D13C9.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/3E89DC53-F05A-E811-9D0F-000101000962.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/40F720A4-405B-E811-817A-000101000922.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/460AEE05-2B5B-E811-9846-000101000925.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/468CDF05-2B5B-E811-9BA9-000101000931.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/64B3E9AF-405B-E811-B2B5-000101000923.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/6E42C913-1D5C-E811-8594-000101000970.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/72CA6978-235B-E811-8FB0-000101000923.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/7A1BA1FC-315B-E811-82F6-000101000936.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/8E8E5B36-485B-E811-B91A-000101000962.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/969D5978-235B-E811-B5F4-00010100092E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/9E454474-235B-E811-8066-000101000933.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/A6A5E7A5-405B-E811-863C-00010100096E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/B6395698-4F5B-E811-9F65-00010100092B.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/C2B4B4AD-405B-E811-BF98-00010100092E.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/C6B635A4-405B-E811-B0CA-001E673CFFC1.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/C8449308-2B5B-E811-9CC0-000101000927.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/D6312BAB-405B-E811-8879-001E6739BC09.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/D83CF170-395B-E811-BAA4-000101000977.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/E86E3A72-395B-E811-8627-001E673D2261.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/EAC4C357-785A-E811-8CBB-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/FE4AF029-485B-E811-A676-001E673D2261.root',
] )